
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def fetch_energy_data():

    api_key = os.getenv("EIA_API_KEY")
    if no api_key:
        print("Error: EIA_API_KEY not set")
        return

    url = "https://api.eia.gov/v2/electricity/retail-sales/data/"
    params = {
        "api_key" : api_key
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
        data = response.json()
        with open("data/raw/energy_data.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Energy data saved successfully.")
        print("Sample record:")
        print(data["response"]["data"][0])
    else:
        print("Failed to fetch energy data. Status code: {response.status_code}")


if __name__ == "__main__":
    fetch_energy_data()                