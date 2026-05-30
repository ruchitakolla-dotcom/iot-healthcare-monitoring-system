import sqlite3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import time

while True:
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, heart_rate, temperature, spo2 FROM health_data")
    rows = cursor.fetchall()

    conn.close()

    if rows:
        ids = [row[0] for row in rows]
        heart_rates = [row[1] for row in rows]
        temperatures = [row[2] for row in rows]
        spo2_values = [row[3] for row in rows]

        plt.figure(figsize=(10, 5))
        plt.plot(ids, heart_rates, marker='o', label='Heart Rate')
        plt.xlabel("Reading ID")
        plt.ylabel("Heart Rate (bpm)")
        plt.title("Heart Rate vs Reading ID")
        plt.grid(True)
        plt.legend()
        plt.savefig("heart_rate.png")
        plt.close()

        plt.figure(figsize=(10, 5))
        plt.plot(ids, temperatures, marker='s', label='Temperature')
        plt.xlabel("Reading ID")
        plt.ylabel("Temperature (°C)")
        plt.title("Temperature vs Reading ID")
        plt.grid(True)
        plt.legend()
        plt.savefig("temperature.png")
        plt.close()

        plt.figure(figsize=(10, 5))
        plt.plot(ids, spo2_values, marker='^', label='SpO2')
        plt.xlabel("Reading ID")
        plt.ylabel("SpO2 (%)")
        plt.title("SpO2 vs Reading ID")
        plt.grid(True)
        plt.legend()
        plt.savefig("spo2.png")
        plt.close()

        print("Graphs updated...")

    else:
        print("No data found.")

    time.sleep(5)
