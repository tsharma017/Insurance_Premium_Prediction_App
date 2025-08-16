**Insurance Premium Prediction App**

This project demonstrates a full-stack machine learning application built with:

FastAPI → backend REST API serving a trained ML model

Streamlit → simple frontend UI for users to interact with the model

scikit-learn → training the machine learning model

pandas / numpy → preprocessing the dataset

Pickle → saving and loading the trained model

📂 Project Structure
├── app.py                # FastAPI app with ML model loading & prediction endpoint
├── main.py               # Alternative FastAPI entrypoint (uvicorn startup)
├── frontend.py           # Streamlit app for user-friendly frontend
├── Fastapi_ml_model.ipynb # Jupyter notebook: model training and export
├── insurance.csv         # Dataset used for training (Insurance Premium data)
├── model.pkl             # Saved trained model (scikit-learn pipeline)
└── README.md             # Documentation

**Setup Instructions**
#1. Clone the repo
git clone https://github.com/your-username/insurance-premium-predictor.git
cd insurance-premium-predictor

#2. Create a virtual environment
python3 -m venv myenv
source myenv/bin/activate   # macOS/Linux
myenv\Scripts\activate      # Windows PowerShell

#3. Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt yet, you can generate one:

pip freeze > requirements.txt

#🚀 Running the App
1. Start the FastAPI backend
uvicorn app:app --host 127.0.0.1 --port 8000 --reload


Verify the API is running at: http://127.0.0.1:8000/docs

2. Start the Streamlit frontend

In another terminal:

streamlit run frontend.py --server.port 8501


Now open: http://127.0.0.1:8501

**📊 Workflow**

Model Training

Run Fastapi_ml_model.ipynb

Loads insurance.csv

Preprocesses features (age, weight, height, income, smoker, city, occupation)

Trains a classification model

Saves it as model.pkl

Backend (FastAPI)

Loads model.pkl

Defines /predict endpoint

Validates user input with Pydantic

Returns JSON with prediction

Frontend (Streamlit)

Collects user input (age, weight, height, income, smoker, city, occupation)

Sends request to FastAPI backend

Displays predicted insurance premium category

📦 Example API Request
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "retired"
}'


Response:

{
  "predicted_category": "medium"
}

**🛠️ Tech Stack**

Python 3.12

FastAPI

Streamlit

scikit-learn

pandas

numpy

**🔮 Future Improvements**

Add probability scores with predictions

Deploy to AWS / Heroku / Render with Docker

Add CI/CD pipeline for model retraining

Secure the API with authentication

👨‍💻 Author

Tejendra Sharma
