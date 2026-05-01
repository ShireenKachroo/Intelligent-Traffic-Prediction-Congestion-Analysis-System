import sqlite3
from datetime import datetime
from src.db.db_connection import get_connection


# -----------------------------
# CREATE TABLE (run once)
# -----------------------------
def create_prediction_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hour INTEGER,
            day INTEGER,
            month INTEGER,
            temp REAL,
            weather TEXT,
            predicted_volume REAL,
            congestion_level TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Prediction table ready!")


# -----------------------------
# STORE SINGLE PREDICTION
# -----------------------------
def store_prediction(input_data, predicted_volume, congestion_level):
    conn = get_connection()
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO predictions (
            hour, day, month, temp, weather,
            predicted_volume, congestion_level, timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        input_data["hour"],
        input_data["day"],
        input_data["month"],
        input_data["temp"],
        input_data["weather"],
        float(predicted_volume),
        congestion_level,
        timestamp
    ))

    conn.commit()
    conn.close()


# -----------------------------
# TEST RUN (optional)
# -----------------------------
if __name__ == "__main__":
    create_prediction_table()

    sample_input = {
        "hour": 8,
        "day": 2,
        "month": 5,
        "temp": 25,
        "weather": "Clear"
    }

    store_prediction(sample_input, 4200, "High")
    print("Sample prediction stored!")