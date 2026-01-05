import requests
import os
import json
from dotenv import load_dotenv

#load variable from .env file
load_dotenv()

def fetch_unemployment_data():
    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        print("Error: FRED_API_KEY not set")
        return

    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id" : "UNRATE",
        "api_key" : api_key,
        "file_type" : "json",
        "frequency" : "m",
        "observation_start" : "2022-01-01" 
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        os.makedirs("data/raw", exist_ok=True)
        data = response.json()
        with open("data/raw/unemployment_data.json","w") as f:
            json.dump(data, f, indent=2)
        print("Unemployment data saved successfully.")
        # Show the most recent observation
        print("Sample record:")
        print(data["observations"][-1])
    else:
        print(f"Failed to fetch unemployment data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_unemployment_data()                    