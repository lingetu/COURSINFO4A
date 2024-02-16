import sqlite3
import csv

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()


# Création des tables

#directors "('mid',)","('pid',)"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS directors (
        mid TEXT,
        pid TEXT,
        FOREIGN KEY (mid) REFERENCES movies(mid),
        FOREIGN KEY (pid) REFERENCES persons(pid),
        PRIMARY KEY (mid, pid)
    )
''')

#characters "('mid',)","('pid',)","('name',)"
cursor.execute('''
               CREATE TABLE IF NOT EXISTS characters (
               mid TEXT,
               pid TEXT,
               name TEXT,
               FOREIGN KEY (mid) REFERENCES movies(mid),
               FOREIGN KEY (pid) REFERENCES persons(pid),
               PRIMARY KEY (mid, pid, name))
               ''')

#genres "('mid',)","('genre',)"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS genres (
        mid TEXT,
        genre TEXT,
        FOREIGN KEY (mid) REFERENCES movies(mid),
        PRIMARY KEY (mid, genre)
    )
''')

# KnownForMovies "('mid',)","('pid',)"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS knownformovies (
        mid TEXT,
        pid TEXT,
        FOREIGN KEY (mid) REFERENCES movies(mid),
        FOREIGN KEY (pid) REFERENCES persons(pid),
        PRIMARY KEY (mid, pid)
    )
''')
# Movies :"('mid',)","('titleType',)","('primaryTitle',)","('originalTitle',)","('isAdult',)","('startYear',)","('endYear',)","('runtimeMinutes',)
# cursor.execute('''DROP TABLE movies''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        mid TEXT PRIMARY KEY,
        titleType TEXT,
        primaryTitle TEXT,
        originalTitle TEXT,
        isAdult INTEGER,
        startYear INTEGER,
        endYear TEXT,
        runtimeMinutes INTEGER
    )
''')

# persons "('pid',)","('primaryName',)","('birthYear',)","('deathYear',)"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        pid TEXT PRIMARY KEY,
        primaryName TEXT,
        birthYear INTEGER,
        deathYear INTEGER
    )
''')
# principals "('mid',)","('ordering',)","('pid',)","('category',)","('job',)"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS principals (
        mid TEXT,
        ordering INTEGER,
        pid TEXT,
        category TEXT,
        job TEXT,
        FOREIGN KEY (mid) REFERENCES movies(mid),
        FOREIGN KEY (pid) REFERENCES persons(pid)
    )
''')

#professions "('pid',)","('jobName',)"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professions (
        pid TEXT,
        jobName TEXT,
        FOREIGN KEY (pid) REFERENCES persons(pid)
    )
''')

#ratings "('mid',)","('averageRating',)","('numVotes',)" 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratings (
        mid TEXT,
        averageRating REAL,
        numVotes INTEGER,
        FOREIGN KEY (mid) REFERENCES movies(mid)
    )
''')

#titles"('mid',)","('ordering',)","('title',)","('region',)","('language',)","('types',)","('attributes',)","('isOriginalTitle',)"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS titles (
        mid TEXT,
        ordering INTEGER,
        title TEXT,
        region TEXT,
        language TEXT,
        types TEXT,
        attributes TEXT,
        isOriginalTitle INTEGER,
        FOREIGN KEY (mid) REFERENCES movies(mid)
    )
''')

#writers "('mid',)","('pid',)"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS writers (
        mid TEXT,
        pid TEXT,
        FOREIGN KEY (mid) REFERENCES movies(mid),
        FOREIGN KEY (pid) REFERENCES persons(pid),
        PRIMARY KEY (mid , pid)
    )
''')



# with open('title.basics.tsv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter='\t')
#     next(reader)  # Skip header
#     for row in reader:
#         cursor.execute('''
#             INSERT INTO title_basics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', row)


# Insertion des données du fichier title.ratings.tsv
# with open('title.ratings.tsv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter='\t')
#     next(reader)  # Skip header
#     for row in reader:
#         cursor.execute('''
#             INSERT INTO title_ratings (tconst, averageRating, numVotes)
#             VALUES (?, ?, ?)
#         ''', row)

# Sauvegarde des modifications et fermeture de la connexion
conn.commit()
cursor.close()
conn.close()