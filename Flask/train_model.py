# train_model.py
import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from data_processing import load_data_from_mongodb, encode_categorical_columns

# Charger et encoder les données
data = load_data_from_mongodb()
data, label_encoders = encode_categorical_columns(data)

# Préparation des données pour le modèle
X = data.drop(['salary', 'salary_currency', 'salary_in_usd'], axis=1)
y = data['salary_in_usd']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle de Gradient Boosting
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)

# Enregistrer le modèle dans un fichier
dump(gb_model, 'gb_model.joblib')
