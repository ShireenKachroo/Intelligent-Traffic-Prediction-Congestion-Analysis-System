import sqlite3

# Connect to database
conn = sqlite3.connect("traffic.db")   # replace with your database name
cursor = conn.cursor()

# Print all tables first
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in Database:")
for table in tables:
    print(table[0])

# Print data from predictions table
print("\nPredictions Table:\n")

cursor.execute("SELECT * FROM predictions")
rows = cursor.fetchall()

# Print column names
column_names = [description[0] for description in cursor.description]
print(column_names)

# Print rows
for row in rows:
    print(row)

conn.close()