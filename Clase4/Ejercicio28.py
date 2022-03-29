dic={}
# indice = "nombre"
# valor="Sebas"

# dic[indice]=valor
# #dic.setdefault(indice,valor)
# print(dic)1


menu =True

while menu:
    op= int(input("Elija una opción:\n1.-Agregar\n2.-Salir\n",end=""))
    if op == 1:
        indice = input("Ingrese el indice: ")
        valor = input("Elija una valor: ")
        dic[indice]=valor
        print(dic,"\n")
    elif op == 2:
        menu = False
    else:
        print("Ingrese una opcion correcta")