import requests

# API URL
url = "https://gnrvoxd4pr7f7wre546m3dw2pq0ruwxb.lambda-url.ap-south-1.on.aws/predict"

# Data to be sent in the POST request
data = {
    "Pregnancies": 3,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 80,
    "BMI": 25.6,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 32
}

# Make the POST request
response = requests.post(url, json=data)

# Print the response from the server
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print(f"Failed to get response, status code: {response.status_code}")
