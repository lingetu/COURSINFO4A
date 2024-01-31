from sklearn.model_selection import KFold
kf=KFold(n_splits=10,shuffle=True)
X=[i for i in range(20)]
print(X)
for learn,test in kf.split(X):
   print("app : ",learn," test ",test)