import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("MYSQL_PASSWORD"),
    database = "energy_pipeline"
)

#load data into pands
df = pd.read_sql("SELECT * FROM energy_unemployment_monthly ORDER BY period", conn)
conn.close()


#conver period to date time for plotting
df['period'] = pd.to_datetime(df['period'], format='%Y-%m')


#plotting
fig, ax1 = plt.subplots(figsize=(12,6))

#plot energy demand
ax1.set_xlabel('Period')
ax1.set_ylabel('Energy(million KWh)', color="blue")
ax1.plot(df['period'], df['sales'], color="blue", label='Energy Demand')
ax1.tick_params(axis='y', labelcolor='blue')

#plot unemployment on secondary axis
ax2=ax1.twinx()
ax2.set_ylabel('Unemployment Rate (%)', color='red')
ax2.plot(df['period'], df['unemployment_rate'], color='red', label='Unemployment Rate')
ax2.tick_params(axis='y', labelcolor='red')

#title and legends
plt.title('Energy Demnad VS Unemployment Rate(Monthly)')
fig.tight_layout()
plt.show(block=True)