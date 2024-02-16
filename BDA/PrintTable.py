import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM genres")

# Récupérer toutes les lignes résultantes
rows = cursor.fetchall()

# Afficher les valeurs récupérées
for row in rows:
    print(row)