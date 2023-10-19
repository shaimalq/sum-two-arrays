t1=[]
t2=[]
T=[]
n=int(input("entrez la taille des tableaux:"))
print("entrez les elements du tableau t1:")
for i in range(n):
    value=int(input())
    t1.append(value)
print("entrez les elements du tableau t2:")
for i in range(n):
    value=int(input())
    t2.append(value)
for i in range(n):
    sum=t1[i]+t2[i]
    T.append(sum)
print(" le tableau T resultant de la somme:",T)