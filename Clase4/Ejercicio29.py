def Imprimir(dicicionario):
    for indice in dicicionario:
        print("Producto:",indice,"Precio:",dicicionario[indice])

dic={}
dic["pan"]=.12
menu=True
while menu:
    op= int(input("Elija una opción:\n1.-Agregar producto\n2.-Facturar\n3.-Salir\n"))
    if op == 1:
        indice = input("Ingrese el indice: ")
        valor = float(input("Ingrese una valor: "))
        dic[indice]=valor
        #print(dic,"\n")
    elif op == 2:
        facturar=True
        while facturar:
            op= int(input("Elija una opción:\n1.-Agregar a factura\n2.-Finalizar\n"))
            if op==1:
                Imprimir(dic)
                total=0
                indice = input("Ingrese el indice: ")
                cantidad = int(input("Ingrese una cantidad: "))
                if dic.get(indice) is None:
                    print("Producto no encontrado :(")
                else:
                    total+=float(dic.get(indice))*cantidad
            else:
                facturar=False

        print("Elm total es: ",total,"\n")
        total=0
    elif op == 3:
        menu = False
    else:
        print("Ingrese una opcion correcta")