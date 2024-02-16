import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()

# Exécuter une requête SQL pour récupérer les films où Jean Reno a joué
cursor.execute('''
    SELECT movies.primaryTitle
    FROM movies
    JOIN principals ON movies.mid = principals.mid
    JOIN persons ON principals.pid = persons.pid
    WHERE persons.primaryName = 'Jean Reno'
''')

# Récupérer les résultats
results = cursor.fetchall()

# Afficher les résultats
if results:
    print("Jean Reno a joué dans les films suivants :")
    for row in results:
        print(row[0])
else:
    print("Jean Reno n'a pas joué dans de films répertoriés dans la base de données.")

# Fermer le curseur et la connexion
cursor.close()
conn.close()
