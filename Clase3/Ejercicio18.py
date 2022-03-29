from random import randint
v= True
aciertos=0
while v:
    op=randint(1,2)
    num1=randint(1,10)
    num2=randint(1,10)
    if (op==1):
        res = num1*num2
        print(num1,"*",num2,"=")
        resUusario=int(input("Ingrese respuesta:"))
        if res==resUusario:
            print("Correcto")
            aciertos+=1
        else:
            print("Incorrecto")
            v=False

print("Tuvo",aciertos,"aciertos :)")