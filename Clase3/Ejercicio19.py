lista = [1,"hola",3.5,False]

while len(lista)>0:
    print(lista)
    elemento=int(input("Ingrese la posicición del elemnto a eliminar: "))
    if elemento>len(lista)-1:
        print("El elemento està fuera de rango")
        continue
    del(lista[elemento])
    print()