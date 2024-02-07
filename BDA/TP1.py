import sqlite3
import csv

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS title_basics (
        tconst TEXT PRIMARY KEY,
        titleType TEXT,
        primaryTitle TEXT,
        originalTitle TEXT,
        isAdult INTEGER,
        startYear INTEGER,
        endYear INTEGER,
        runtimeMinutes INTEGER,
        genres TEXT
    )
''')

with open('title.basics.tsv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip header
    for row in reader:
        cursor.execute('''
            INSERT INTO title_basics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

# Création de la table title_ratings
cursor.execute('''
    CREATE TABLE IF NOT EXISTS title_ratings (
        tconst TEXT PRIMARY KEY,
        averageRating REAL,
        numVotes INTEGER,
        FOREIGN KEY (tconst) REFERENCES title_basics (tconst)
    )
''')

# Insertion des données du fichier title.ratings.tsv
with open('title.ratings.tsv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip header
    for row in reader:
        cursor.execute('''
            INSERT INTO title_ratings (tconst, averageRating, numVotes)
            VALUES (?, ?, ?)
        ''', row)

# Sauvegarde des modifications et fermeture de la connexion
conn.commit()
conn.close()