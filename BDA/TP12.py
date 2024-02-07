import sqlite3
import csv

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()

csv_file = 'DBTINY/characters.csv'

# Open the CSV file and insert the data into the table
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO characters (mid, pid, name)
            VALUES (?, ?, ?)
        ''', row)

# Sauvegarde des modifications et fermeture de la connexion
conn.commit()
conn.close()
