from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

## DATA CLEANING
# loading dataset
df1 = pd.read_csv("autoplius.csv")
df1.head()

# converting Gearbox into a dummy variable
GearboxDummy = pd.get_dummies(df1[["Gearbox"]])
GearboxDummy.head()

# altering the dataset
df1 = pd.concat([df1, GearboxDummy], axis=1).drop(
    ["Gearbox", "Marque", "CarType", "FuelType"], axis=1
)

# checking for wrong values
df1.Engine_l.unique()

# deleting rows with wrong values from the dataframe (227 rows)
engine_str = [
    "wagon",
    "mpv",
    "pick-up",
    "saloon",
    "suv",
    "hatchback",
    "passenger",
    "commercial",
    "coupe",
    "other",
]
df1 = df1[~df1["Engine_l"].isin(engine_str)]

# converting Engine_l into float variable
df1.Engine_l = df1.Engine_l.astype("float")

# checking for null values
df1.isnull().any()

# deleting rows with Na values
df1 = df1.dropna()

# reseting the index after dropping NaN rows
df1 = df1.reset_index(drop=True)

## MODELLING PART
# scaling only features

scaler = StandardScaler()
features = [
    "ManufacturingDate",
    "Engine_l",
    "Power_kW",
    "Mileage_km",
    "Gearbox_Automatic",
    "Gearbox_Manual",
]
scaled_features = pd.DataFrame(scaler.fit_transform(df1[features]), columns=features)

# merging scaled features with the Price column
data = pd.concat([scaled_features, df1.Price_euro], axis=1)

# dividing dataset into train and test subsets

x_train2, x_test2, y_train2, y_test2 = train_test_split(
    data[features], data.Price_euro, random_state=8, train_size=0.7
)

# training the regression model

lrmodel = LinearRegression()
lrmodel.fit(x_train2, y_train2)

# evaluating the trained model

predicted2 = lrmodel.predict(x_test2)
expected2 = y_test2

print(f"Mean Squared Error: {round(mean_squared_error(expected2, predicted2), 2)}")
print(f"R2 Score: {round(r2_score(expected2, predicted2), 2)}")


# saving model to file
pickle.dump(lrmodel, open("model\lrmodel.pkl", "wb"))

# saving scaler to file
pickle.dump(scaler, open("model\scaler.pkl", "wb"))
