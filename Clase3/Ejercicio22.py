from random import randint
from re import L

def LlenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista


def LlenarAle(n):
    lista=[]
    num=randint(1,n)
    lista+=[num]
    for i in range(1,n-1):
        while num in lista:
            num=randint(1,n)
        lista+=[num]
    return lista

listaA=LlenarSec(10)
##print(listaA)
listaB = LlenarAle(10)
##print(listaB)

for i in range(len(listaA)-1):
    print("A la persona",listaA[i],"le tocó con la persona",listaB[i])

