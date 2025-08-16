# --- Import required libraries ---
from fastapi import FastAPI, Path, Query, HTTPException           # Core FastAPI utilities
from fastapi.responses import JSONResponse                       # For custom JSON responses
from pydantic import BaseModel, Field, computed_field             # For request body validation
from typing import Annotated, Literal, Optional                           # For type hints & constraints
from pathlib import Path as _Path                                 # For file handling
import json                                                       # For reading/writing JSON files


# --- Initialize FastAPI application ---
app = FastAPI()

# Path to store patient data (JSON file)
DATA_PATH = _Path("patients.json")


# --- Define Patient model using Pydantic ---
class Patient(BaseModel):
    """
    Represents a patient with basic details.
    Pydantic validates input automatically based on these type hints & constraints.
    """

    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient lives")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[
        Literal["male", "female", "other"],
        Field(..., description="Gender of the patient")
    ]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kilograms")]

    # Computed field: BMI
    @computed_field(return_type=float)
    def bmi(self) -> float:
        """Calculate BMI from height & weight."""
        return round(self.weight / (self.height ** 2), 2)

    # Computed field: Health verdict based on BMI
    @computed_field(return_type=str)
    def verdict(self) -> str:
        """Categorize patient health based on BMI."""
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        else:
            return "Overweight/Obese"

# New update pydantic model 

class PatientUpdate(BaseModel):
    # id not it's as path parametr not as request body parameter.
    name: Annotated[Optional[str], Field(default=None)]  # use Optional
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    gender: Annotated[
       Optional[ Literal["male", "female", "other"]],
        Field(default=None)
    ]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]


# --- Utility Functions for File I/O ---
def load_data() -> dict:
    """
    Reads patient data from patients.json file.
    If file doesn't exist, returns an empty dictionary.
    """
    if not DATA_PATH.exists():
        return {}
    with DATA_PATH.open("r") as f:
        return json.load(f)


def save_data(data: dict) -> None:
    """
    Saves patient data to patients.json file.
    """
    with DATA_PATH.open("w") as f:
        json.dump(data, f, indent=2)


# --- API Routes ---
@app.get("/")
def hello():
    """Root endpoint to check if API is running."""
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    """Provides description of the API."""
    return {"message": "A fully functional API to manage your patient records"}


@app.get("/view")
def view():
    """View all patient records."""
    return load_data()


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")
):
    """
    View details of a specific patient by ID.
    Raises 404 if patient not found.
    """
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on height, weight, or bmi"),
    order: str = Query("asc", description="Sort order: asc or desc"),
):
    """
    Sort patients based on height, weight, or BMI.
    """
    valid_fields = {"height", "weight", "bmi"}

    # Validate sort field
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field; choose from {sorted(valid_fields)}")

    # Validate order
    if order not in {"asc", "desc"}:
        raise HTTPException(status_code=400, detail="Invalid order; choose 'asc' or 'desc'")

    data = load_data()
    reverse = order == "desc"

    # Sort and return patients
    return sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=reverse)


@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    data[patient.id] = patient.model_dump()
    save_data(data)
    return JSONResponse(status_code=201, content={"message": "Patient created successfully", "id": patient.id})


# update endpoint 
@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    existing_patient_info = data[patient_id]

    # converting in dictonary by using model_dump
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, vlaue in updated_patient_info.values():
        existing_patient_info[key] = vlaue 

    # existing_patient_info –> pydantic object -> update bmi + verdict 
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    # -> pydantic object -> dict 
    existing_patient_info = patient_pydantic_obj.model_dump(exclude = 'id')

    # add this dict to data 
    data[patient_id] = existing_patient_info

    # save data 
    save_data(data)

    return JSONResponse(status_code = 200, content={'message':'patient updated'})

# to dele the information from the data through data delete end point 
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = 'Patient not found')

    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'patient deleted'})