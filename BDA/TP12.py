import sqlite3
import csv

# Connexion à la base de données SQLite
conn = sqlite3.connect('imdb_database.db')
cursor = conn.cursor()


# # Open the CSV file and insert the data into the table
# with open("characters.csv", 'r', newline='', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)  # Skip the header row
#     for row in csv_reader:
#         cursor.execute('''
#             INSERT INTO characters (mid, pid, name)
#             VALUES (?, ?, ?)
#         ''', row)

with open("directors.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO directors (mid, pid)
            VALUES (?, ?)
        ''', row)     

with open("genres.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO genres (mid, genre)
            VALUES (?, ?)
        ''', row)

with open("knownformovies.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO knownformovies (mid, pid)
            VALUES (?, ?)
        ''', row)     

#"('mid',)","('titleType',)","('primaryTitle',)","('originalTitle',)","('isAdult',)","('startYear',)","('endYear',)","('runtimeMinutes',)"
with open("movies.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO movies (mid, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)    

#"('pid',)","('primaryName',)","('birthYear',)","('deathYear',)"
with open("persons.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO persons (pid, primaryName, birthYear, deathYear)
            VALUES (?, ?, ?, ?)
        ''', row)
        
#"('mid',)","('ordering',)","('pid',)","('category',)","('job',)"
with open("principals.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO principals (mid, ordering, pid, category, job)
            VALUES (?, ?, ?, ?, ?)
        ''', row)


#"('pid',)","('jobName',)"
with open("professions.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO professions (pid, jobName)
            VALUES (?, ?)
        ''', row)   


#"('mid',)","('averageRating',)","('numVotes',)"
with open("ratings.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO ratings (mid, averageRating, numVotes)
            VALUES (?, ?, ?)
        ''', row)   
#"('mid',)","('ordering',)","('title',)","('region',)","('language',)","('types',)","('attributes',)","('isOriginalTitle',)"
with open("titles.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO titles (mid, ordering, title, region, language, types, attributes, isOriginalTitle)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)
#"('mid',)","('pid',)"
with open("writers.csv", 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO writers (mid, pid)
            VALUES (?, ?)
        ''', row)



# Sauvegarde des modifications et fermeture de la connexion
conn.commit()
cursor.close()
conn.close()
