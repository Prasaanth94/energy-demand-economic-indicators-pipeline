import json  
import os
import pandas as pd

def transform_unemployment_data():
    #load raw json
    with open("data/raw/unemployment_data.json") as f:
        raw_data = json.load(f)

    #extract list of observations
    records = raw_data["observations"]

    #convert to DataFrame
    df = pd.DataFrame(records)

    #keep only date and value
    df = df[["date", "value"]]

    #Convert value to float
    df["value"] = pd.to_numeric(df["value"], errors ='coerce')

    #drop rows with missing value
    df = df.dropna(subset=["value"])

    #convert date to yyyy-mm for joining
    df["period"] = df["date"].str[:7]


    #rename column for clarity
    df.rename(columns={"value": "unemployment_rate"}, inplace=True)

    #save transformed data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/unemployment_transformed.csv", index=False)
    print("Unemployment data transformed and saved.")
    print(df.head())


if __name__ == "__main__":
    transform_unemployment_data()