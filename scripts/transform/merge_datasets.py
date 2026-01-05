import pandas as pd
import os

def merge_energy_and_unemployment():
    #load processed datasets
    energy_df = pd.read_csv("data/processed/energy_transformed.csv")
    unemployment_df = pd.read_csv("data/processed/unemployment_transformed.csv")

    print("Energy periods:")
    print(energy_df["period"].sort_values().unique())

    print("\nunemployment periods:")
    print(unemployment_df["period"].sort_values().unique())


    common_periods = set(energy_df["period"]).intersection(
        set(unemployment_df["period"])
    )

    if not common_periods:
        raise ValueError("No overlapping periods between datasets")


    #Fliter both datasets to overlapping periods only
    energy_df = energy_df[energy_df["period"].isin(common_periods)]
    unemployment_df = unemployment_df[unemployment_df["period"].isin(common_periods)]

    #merge
    merged_df = pd.merge(
        energy_df,
        unemployment_df,
        on = "period",
        how = "inner"
    )

    #save merged dataset
    os.makedirs("data/final", exist_ok=True)
    merged_df.to_csv("data/final/energy_employment_merged.csv", index=False)

    print("Datasets merged successfully.")
    print(merged_df.head())


if __name__ == "__main__":
    merge_energy_and_unemployment()    