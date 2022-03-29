def LlenarSecuencial(n):
    tabla=[]
    numero=1
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[numero]
            numero+=1
    return tabla

def Imprimir(tabla):
    for i in tabla:
            print(i)

table=LlenarSecuencial(10)
Imprimir(table)