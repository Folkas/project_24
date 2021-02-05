import pickle
import json
from flask import Flask, request
import numpy as np
from preprocessing import preprocessing_function
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# path to the saved .pkl files
mpath = "model/lrmodel.pkl"
spath = "model/scaler.pkl"

# loading the model file
lrmodel = pickle.load(open(mpath, "rb"))
scaler = pickle.load(open(spath, "rb"))

app = Flask(__name__)


@app.route("/cars", methods=["GET", "POST"])
def car() -> str:
    """
    If method POST:

    Predicts car price for the input data. Firstly,
    the function preprocesses the input parameters for the request data using standard scalling.
    Then it passes the input to the trained model and returns predicted price.

    Parameters:

    Six car price features put into a list: ManufacturingDate (int), Engine_l (float), Power_kW (float), Mileage_km (float),
    Gearbo_Automatic (binary: 0 for no, 1 for yes) and Gearbox_Manual (binary: 0 for no, 1 for yes)

    Returns:

    Predicted car price in euros (int)

    If method GET:

    Parameters:

    None

    Returns:

    The list of 10 most recent requests and price predictions in JSON format
    """
    if request.method == "POST":
        input_params = preprocessing_function(request.data)
        # standard scaling the input_params
        scaled_params = scaler.transform(input_params)
        try:
            prediction = lrmodel.predict(scaled_params.tolist())
        except:
            return json.dumps({"error": "PREDICTION FAILED"}), 400

        # uploading inputs into database table
        load_dotenv(override=True)
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = connection.cursor()
        for i, m in zip(prediction, input_params):
            cur.execute(
                f"INSERT INTO autoplius(\
                manufacturingDate, engine_l, power_kw, mileage_km, gearbox_auto, gearbox_manual, price_euro) \
                VALUES('{int(m[0])}', '{m[1]}', '{m[2]}', '{m[3]}', '{int(m[4])}', '{int(m[5])}', '{int(i)}')"
            )
        connection.commit()
        return json.dumps({"Predicted price": prediction.tolist()})

    if request.method == "GET":
        try:
            load_dotenv(override=True)
            connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            cur = connection.cursor()
            # collecting list of all cars
            cur.execute("SELECT * from autoplius ORDER BY id DESC LIMIT 10;")
            rows = cur.fetchall()
            cars = [
                {
                    "id": row[0],
                    "manufacturingDate": row[1],
                    "engine_l": row[2],
                    "power_kw": row[3],
                    "mileage_km": row[4],
                    "gearbox_auto": row[5],
                    "gearbox_manual": row[6],
                    "price_euro": row[7],
                }
                for row in rows
            ]
            return json.dumps({"Last 10 inputs and predictions": cars})
        except:
            return json.dumps({"error": "CANNOT RETRIEVE USERS"}), 500


if __name__ == "__main__":
    app.run()
