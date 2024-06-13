import requests
import pandas as pd
from pymongo import MongoClient
from io import StringIO

def load_data():
    url = "https://ai-jobs.net/salaries/download/salaries.csv"
    response = requests.get(url, verify=False)  # La vérification SSL est désactivée
    if response.status_code == 200:
        data = pd.read_csv(StringIO(response.text))
        client = MongoClient("mongodb://localhost:27017/Salary")
        db = client.Salary
        collection = db.SDV_Project
        collection.insert_many(data.to_dict('records'))
        print("Données chargées avec succès dans MongoDB")
    else:
        print("Erreur lors du téléchargement du fichier")

if __name__ == "__main__":
    load_data()