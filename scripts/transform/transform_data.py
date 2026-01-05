import json
import os
import pandas as pd

def transform_energy_data():
    #load raw json
    with open("data/raw/energy_data.json") as f:
        raw_data = json.load(f)

    #extract list of records
    records = raw_data["response"]["data"]    

    #conver to DataFrame
    df = pd.DataFrame(records)

    #keep only necessary columns
    df = df[["period", "sales"]]

    #conver sales to float
    df["sales"] = df["sales"].astype(float)

    #Group by month (sum across states)
    df_grouped = df.groupby("period", as_index=False).sum()

    

    #Save transformed Data
    os.makedirs("data/processed",exist_ok=True)
    df_grouped.to_csv("data/processed/energy_transformed.csv", index=False)
    print("Energy Data transformed and saved.")


if __name__ == "__main__":
    transform_energy_data()