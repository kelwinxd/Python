import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.kel'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'keltable'

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} "
    "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)"
)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Imprimir o nome das tabelas
print("Tabelas no banco de dados:")
for tabela in tabelas:
    print(tabela[0])


con.commit()
