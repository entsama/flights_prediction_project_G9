from flask import Flask, render_template, request, jsonify
from joblib import load
import pandas as pd
from data_processing import load_data_from_mongodb, encode_categorical_columns
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Activer CORS pour toute l'application

# Charger et encoder les données
data = load_data_from_mongodb()
data, label_encoders = encode_categorical_columns(data)

# Charger le modèle à partir du fichier
gb_model = load('gb_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_salary():
    try:
        input_data = request.get_json()
        app.logger.info(f"Received input data: {input_data}")

        input_df = pd.DataFrame([input_data])
        app.logger.info(f"DataFrame before encoding: {input_df}")

        for col in label_encoders:
            if col in input_df.columns:
                input_df[col] = label_encoders[col].transform(input_df[col])
        
        app.logger.info(f"DataFrame after encoding: {input_df}")

        predicted_salary = gb_model.predict(input_df)
        app.logger.info(f"Predicted salary: {predicted_salary[0]}")

        return jsonify({'predicted_salary': float(predicted_salary[0])})
    except Exception as e:
        app.logger.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
