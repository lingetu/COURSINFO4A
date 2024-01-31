
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Charger le jeu de données iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Définir le nombre de voisins
nb_voisins = 15

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer le classifieur des k plus proches voisins
clf = neighbors.KNeighborsClassifier(n_neighbors=nb_voisins)

# Entraîner le modèle
clf.fit(X_train, y_train)

# Prédire les classes sur l'ensemble de test
y_pred = clf.predict(X_test)

# Calculer et afficher la précision du modèle sur l'ensemble de test
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle sur l'ensemble de test:", accuracy)