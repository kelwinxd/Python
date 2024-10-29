import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")
rows = cursor.fetchall()

for row in rows:
   print(row)

cursor.close()
con.close()