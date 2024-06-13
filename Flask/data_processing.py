# data_processing.py
import pandas as pd
from pymongo import MongoClient
from sklearn.preprocessing import LabelEncoder

def load_data_from_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['Salary']
    collection = db['SDV_Project']
    data = pd.DataFrame(list(collection.find()))
    data.drop('_id', axis=1, inplace=True)
    return data

def encode_categorical_columns(data):
    label_encoders = {}
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le
    return data, label_encoders
