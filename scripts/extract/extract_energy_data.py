
import requests
import os

def fect_energy_data():
    url = "https://api.eia.gov/v2/electricity/retail-sales/data/"
    params = {
        "frequency" : "monthly",
        "data[0]" : "sales",
        "facets[sectorid][]" : "ALL",
        "sort[0][column]" : "period",
        "sort[0][direction]" : "desc",
        "length" : 24
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/energy_data.json", "w") as f:
            f.write(response.text)
        print("Energy data saved successfully.")
    else:
        print("Failed to fetch energy data.")


if __name__ == "__main__":
    fetch_energy_data()                