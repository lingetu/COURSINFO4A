from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random # pour pouvoir utiliser un g ́en ́erateur de nombres al ́eatoires

from sklearn.datasets import load_iris
irisData=load_iris()

X=irisData.data
Y=irisData.target
nb_voisins=15

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=random.seed())
#nombre d'élément dans l'echantillon d'apprentissage

print(len(X_train))

#nombre d'élément dans l'echantillon de test ---Somme des deux = 150 soit nombre d'élément dans l'echantillon total test-_size = 0.3 donc 30% de 150 = 45
print(len(X_test))

#Nombre d'élément dans chaque classe de l'echantillon d'apprentissage
#nombre d'élément dans la classe 0
len(X_train[Y_train==0])
#nombre d'élément dans la classe 1
len(X_train[Y_train==1])
#nombre d'élément dans la classe 2
len(X_train[Y_train==2])


#Création du classifieur des k plus proches voisins avec 15 voisins
clf = neighbors.KNeighborsClassifier(n_neighbors=nb_voisins)

clf.fit(X_train, Y_train)

Z = clf.predict(X_test)
print(clf.score(X_test,Y_test))
print(X_test[Z!=Y_test])