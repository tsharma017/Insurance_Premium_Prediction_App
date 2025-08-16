**Insurance Premium Prediction App**

This project demonstrates a full-stack machine learning application for predicting insurance premium categories.

It combines:

FastAPI → Backend REST API serving a trained ML model

Streamlit → User-friendly frontend UI

scikit-learn → Model training

pandas / numpy → Data preprocessing

Pickle → Model saving and loading
```
📂 Project Structure
├── app.py                 # FastAPI app (API + ML model prediction endpoint)
├── main.py                # Alternative FastAPI entrypoint (uvicorn startup)
├── frontend.py            # Streamlit frontend (user interface)
├── Fastapi_ml_model.ipynb # Jupyter notebook (model training & export)
├── insurance.csv          # Dataset used for training
├── model.pkl              # Trained model (saved with pickle)
└── README.md              # Documentation
```

⚙️ Setup Instructions
1. Clone the Repository
```
git clone https://github.com/tsharma017/Insurance_Premium_Prediction_App.git
cd Insurance_Premium_Prediction_App
```

3. Create a Virtual Environment
```
python3 -m venv myenv
```

Activate the environment:
macOS / Linux
```
source myenv/bin/activate
```

Windows PowerShell
```
myenv\Scripts\activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

👉 If you don’t have a requirements.txt, generate one:
```
pip freeze > requirements.txt
```
🚀 Running the App
1. Start the FastAPI Backend
```
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

✅ Open API docs at: http://127.0.0.1:8000/docs

2. Start the Streamlit Frontend

In another terminal:
```
streamlit run frontend.py --server.port 8501
```

✅ Open frontend at: http://127.0.0.1:8501

📊 Workflow
Model Training

Run *Fastapi_ml_model.ipynb*

Loads insurance.csv dataset

Preprocesses features:

- age

- weight

- height

- income

- smoker

- city

- occupation

Trains a classification model

Saves trained model as model.pkl

**Backend (FastAPI)**

Loads model.pkl

Defines /predict endpoint

Uses Pydantic for input validation

Returns JSON with prediction

**Frontend (Streamlit)**

Collects user input through a form

Sends request to backend API

Displays predicted insurance premium category

📦 Example API Request

Request:
```

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

```

Response:
```
{
  "predicted_category": "medium"
}
```

🛠️ Tech Stack

Python 3.12

FastAPI

Streamlit

scikit-learn

pandas

numpy

🔮 Future Improvements

Add probability scores with predictions

Deploy to AWS / Heroku / Render with Docker

Add CI/CD pipeline for model retraining

Expand dataset with more health & lifestyle features
