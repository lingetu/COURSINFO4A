from sklearn.datasets import load_iris # les donn ́ees iris sont charg ́ees
import pylab as pl # permet de remplacer le nom "pylab" par "pl"
irisData=load_iris()



# len(irisData.data)
# help(len) # pour quitter l’aide, tapez ’q’ (pour quit)
# irisData.target_names[0]
# irisData.target_names[2]
# irisData.target_names[-1]
# irisData.target_names[len(irisData.target_names)-1]
# irisData.data.shape
# irisData.data[0]
# irisData.data[0][1]
# irisData.data[:,1]

# print(irisData.data)
# print(irisData.target)
# print(irisData.target_names)
# print(irisData.feature_names)
# print(irisData.DESCR)


# X=irisData.data
# Y=irisData.target
# x = 0
# y = 1
# pl.scatter(X[:, x], X[:, y],c=Y) 
# # les fonctions
# # d ́efinies dans une librairie doivent ^etre pr ́efix ́ees par son nom
# pl.show()
# help(pl.scatter)
# pl.xlabel(irisData.feature_names[x])
# pl.ylabel(irisData.feature_names[y])
# pl.scatter(X[:, x], X[:, y],c=Y)
# pl.show()



#MEthode 2 
# import pylab as pl
# X=irisData.data
# Y=irisData.target
# x = 0
# y = 1
# Y==0
# X[Y==0]
# X[Y==0][:, x]
# pl.scatter(X[Y==0][:, x],X[Y==0][:,y],
# color="red",label=irisData.target_names[0])
# pl.scatter(X[Y==1][:, x],X[Y==1][:, y],
# color="green",label=irisData.target_names[1])
# pl.scatter(X[Y==2][:, x],X[Y==2][:, y],
# color="blue",label=irisData.target_names[2])
# pl.legend()
# pl.show()
#methode 3 
