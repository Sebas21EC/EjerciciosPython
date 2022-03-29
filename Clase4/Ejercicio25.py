def Imprimir(tabal):
    for i in range(len(tabal)):
        print("[",end="")
        for j in range(len(tabal)):
            print("%3s"%tabal[i][j],end="")
        print("]")

def LLenarVacio(n):
    tabla=[]
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[" "]
    return tabla

def Asteriscos(tabla,simbolo):
    if len(tabla)%2==0:
        print("La songitud debe ser impar")
    else:
        for i in range(len(tabla)):
            for j in range(len(tabla)):
                if i == len(tabla)//2 or j==len(tabla)//2 or i==j or (i+j)==len(tabla)-1:
                    tabla[i][j]=simbolo
        Imprimir(tabla)


tabla =LLenarVacio(11)
Asteriscos(tabla,"*")
