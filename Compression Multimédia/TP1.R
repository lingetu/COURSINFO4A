proba<-0.5
iterations<-0

x1<-rbinom(n=1000,size=1,prob=proba)
x1


RLECOD <- function (b, T, m, C, comp) # b = bit répété, m = taille bloc, C = tableau codé 
 # comp = taux de compression 
p = 0.9 
T = float (runif (n, 0, 1/p))
C = T [1] 
n = length (T) 
d = 2^m – 1 # longueur max de codage d’un bloc 
k = 0 # compteur des suites de bits 
for (j in 1 : n) 
{ 
 if ( T [j] == b) 
 { 
 k <- k + 1 } 
 else { 
 l = k 
 k = 0 
 q = floor (l/d) 
 r = l – d*q 
 C0 = cbind (rep(1, m*q)) 
 * C1 = decimal2binary (r, m) 
 C2 = cbind (C0, C1) 
 C <- cbind (C, C2) 
 } 
 } 
 C <- cbind (C, T [n]) 
 nc = length (C) 
 comp = 1 – nc/c