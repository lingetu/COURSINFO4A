from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.model_selection import KFold
import random
import pylab as pl
digits=load_digits()


X=digits.data
Y=digits.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=random.seed())
X_train2,X_test2,Y_train2,Y_test2=train_test_split(X_train,Y_train,test_size=0.5,random_state=random.seed())


# digits.data[0]
# digits.images[0]
# print(digits.images[0])
# pl.matshow(digits.images[0])
# digits.data[0].reshape(8,8)
# digits.target[0]
n_split=10



###########################################################################################
#Methode train_test_split
scores=[]
for k in range(1,30):
    score=0
    clf = neighbors.KNeighborsClassifier(k)
    #for learn,test in kf:
    clf.fit(X_train2, Y_train2)
    score = score + clf.score(X_test2,Y_test2)
    scores.append(score)    
    print(["{:4.4f}".format(s) for s in scores])
    print("meilleure valeur pour k : ",scores.index(max(scores))+1)

koptimal=scores.index(max(scores))+1
clf2 = neighbors.KNeighborsClassifier(koptimal)
clf2.fit(X_train, Y_train)
print(clf2.score(X_test,Y_test))

###########################################################################################
#Methode KFold
# kf=KFold(n_splits=n_split,shuffle=True)
# scores=[]
# for k in range(1,30):
#     score=0
#     clf = neighbors.KNeighborsClassifier(k)
#     for learn,test in kf.split(X_train):
#         X_train2=X_train[learn]
#         Y_train2=Y_train[learn]
#         clf.fit(X_train2, Y_train2)
#         X_test2=X_train[test]
#         Y_test2=Y_train[test]
#         score = score + clf.score(X_test2,Y_test2)
#     scores.append(score/n_split)
# print(["{:4.4f}".format(s) for s in scores])
# print("meilleure valeur pour k : ",scores.index(max(scores))+1)


# pl.gray()
# pl.matshow(digits.images[0])
# pl.show()
