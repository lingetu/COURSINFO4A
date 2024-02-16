import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()

# Exécuter une requête SQL pour récupérer les trois meilleurs films d'horreur des années 2000
cursor.execute('''
    SELECT movies.primaryTitle, ratings.averageRating
    FROM movies
    JOIN genres ON movies.mid = genres.mid
    JOIN ratings ON movies.mid = ratings.mid
    WHERE genres.genre = 'Horror'
        AND movies.startYear BETWEEN 2000 AND 2009
    ORDER BY ratings.averageRating DESC
    LIMIT 3
''')

# Récupérer les résultats
results = cursor.fetchall()