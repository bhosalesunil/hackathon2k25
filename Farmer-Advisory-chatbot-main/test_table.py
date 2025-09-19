import sqlite3

conn = sqlite3.connect("queries.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

conn.close()


import sqlite3

def insert_data():
    conn = sqlite3.connect("queries.db")
    cursor = conn.cursor()
    
    question = "What is the weather?"
    response = "It is sunny today."
    
    cursor.execute("INSERT INTO queries (question, response) VALUES (?, ?)", (question, response))
    conn.commit()
    conn.close()
    
    print("✅ Data inserted.")

insert_data()