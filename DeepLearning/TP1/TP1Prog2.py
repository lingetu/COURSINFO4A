
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data
Y = iris.target

nb_voisins = 15
# help(neighbors.KNeighborsClassifier)
clf = neighbors.KNeighborsClassifier(nb_voisins)
# help(clf.fit)
clf.fit(X, Y)
# help(clf.predict)
print(clf.predict([[ 5.4, 3.2, 1.6, 0.4]]))
print(clf.predict_proba([[ 5.4, 3.2, 1.6, 0.4]]))
print(clf.score(X,Y))
Z = clf.predict(X)
print(X[Z!=Y])