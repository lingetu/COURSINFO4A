import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()

# Liste des noms de table
tables = ['directors', 'characters', 'genres', 'knownformovies', 'movies', 'persons', 'principals', 'professions', 'ratings', 'titles', 'writers','title_basics']

# Supprimer chaque table
# for table in tables:
#     cursor.execute(f'DROP TABLE IF EXISTS {table}')

cursor.execute('DROP TABLE IF EXISTS persons')

# Valider les suppressions
conn.commit()

# Fermer la connexion
conn.close()
