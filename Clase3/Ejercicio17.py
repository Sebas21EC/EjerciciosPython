saldo=0
op=0
while (op!=3):
    op = int (input("Ingrese una opcion:\n1.Deposito.\n2.Retiro.\n3.Salir\n"))
    if(op>3 and op <=0):
        print("Opcion invaldia")
    else:
        if op==1:
            cant = float (input("Ingrese el valor a depositar:"))
            saldo+=cant
        if op==2:
            cant = float (input("Ingrese el valor a retirar:"))
            saldo-=cant if cant-saldo<0 else print("No puede retir esa cantidad porque exede de su saldo")
        if op==3:
            print("Saliendo.....................")
    
print("Su saldo total es de:",saldo)