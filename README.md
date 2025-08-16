🛡️ Insurance Premium Prediction App

This project demonstrates a full-stack machine learning application for predicting insurance premium categories. It combines:

FastAPI → Backend REST API serving a trained ML model

Streamlit → User-friendly frontend UI

scikit-learn → Machine learning model training

pandas / numpy → Data preprocessing

Pickle → Model saving and loading

📂 Project Structure
├── app.py                 # FastAPI app (API + ML model prediction endpoint)
├── main.py                # Alternative FastAPI entrypoint (uvicorn startup)
├── frontend.py            # Streamlit frontend (user interface)
├── Fastapi_ml_model.ipynb # Jupyter notebook (model training & export)
├── insurance.csv          # Dataset used for training
├── model.pkl              # Trained model (saved with pickle)
└── README.md              # Documentation

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/tsharma017/Insurance_Premium_Prediction_App.git
cd Insurance_Premium_Prediction_App

2. Create a virtual environment
python3 -m venv myenv
source myenv/bin/activate   # macOS/Linux
myenv\Scripts\activate      # Windows PowerShell

3. Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, generate one:

pip freeze > requirements.txt

🚀 Running the App
1. Start the FastAPI backend
uvicorn app:app --host 127.0.0.1 --port 8000 --reload


Now visit: http://127.0.0.1:8000/docs
(You can test the API interactively here!)

2. Start the Streamlit frontend

Open a new terminal and run:

streamlit run frontend.py --server.port 8501


Now visit: http://127.0.0.1:8501

📊 Workflow
🔹 Model Training

Run Fastapi_ml_model.ipynb

Loads insurance.csv

Preprocesses features:
(age, weight, height, income, smoker, city, occupation)

Trains a classification model

Saves trained model as model.pkl

🔹 Backend (FastAPI)

Loads model.pkl

Defines /predict endpoint

Validates user input with Pydantic

Returns JSON prediction

🔹 Frontend (Streamlit)

Collects user input (form)

Sends request to FastAPI backend

Displays predicted premium category

📦 Example API Request
Request
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

Response
{
  "predicted_category": "medium"
}

🛠️ Tech Stack

Python 3.12

FastAPI

Streamlit

scikit-learn

pandas

numpy

🔮 Future Improvements

Add probability scores with predictions

Deploy app to AWS / Heroku / Render using Docker

Add CI/CD pipeline for automatic model retraining

Extend dataset with more features (health conditions, lifestyle habits, etc.)

👨‍💻 Author

Tejendra Sharma
📌 GitHub Profile
