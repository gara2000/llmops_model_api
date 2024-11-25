from flask import Flask, request, jsonify
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.joblib')

# Define the /predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Preprocess and convert the input data into a numpy array
    input_data = np.array(data['instances'])

    # Perform prediction using the model
    predictions = model.predict(input_data)

    # Return the predictions as a JSON response
    return jsonify({'predictions': predictions.tolist()})

@app.route('/predict', methods=['GET'])
def describe():
    return 'This is the prediction URL!!!!\n'

# Run the app if this file is run directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
