from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.responses import JSONResponse
import uvicorn
from mangum import Mangum


# Load the trained model
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize FastAPI
app=FastAPI()
handler=Mangum(app)

# Define the request body structure
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Define prediction endpoint
@app.post("/predict")
def predict_diabetes(input_data: DiabetesInput):
    # Convert input to numpy array
    data = np.array([[input_data.Pregnancies, input_data.Glucose, input_data.BloodPressure,
                      input_data.SkinThickness, input_data.Insulin, input_data.BMI,
                      input_data.DiabetesPedigreeFunction, input_data.Age]])

    # Make prediction
    prediction = model.predict(data)
    result = "Diabetic" if prediction[0] == 1 else "Non-diabetic"
    return JSONResponse({"prediction": result})


if __name__=="__main__":
  uvicorn.run(app,host="0.0.0.0",port=9000)
