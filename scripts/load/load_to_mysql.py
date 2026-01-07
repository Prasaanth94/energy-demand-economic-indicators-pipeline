import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def load_data_to_mysql():
    #load merged csv
    df = pd.read_csv("data/final/energy_unemployment_merged.csv")

    #connecting to mysql
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = os.getenv("MYSQL_PASSWORD"),
        database = "energy_pipeline"
    )

    cursor = connection.cursor()

    insert_query = """
        INSERT INTO energy_unemployment_monthly (period, sales, unemployment_rate)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            SALES = VALUES(sales),
            unemployment_rate = VALUES(unemployment_rate);
    """

    for _, row in df.iterrows():
        cursor.execute(
            insert_query,
            (row["period"], row["sales"], row["unemployment_rate"])
        )
    
    connection.commit()
    print(f"Data loaded successfully into energy_unemployment_monthly({len(df)}rows).")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    load_data_to_mysql();    