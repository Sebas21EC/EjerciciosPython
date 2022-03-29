from random import randint
gana_usuario=0
gana_maquina=0
def Texto(n):
    return "PIEDRA" if n==1 else "PAPEL" if n==2 else "TIJERA"

while gana_usuario<3 and gana_maquina<3:
    opcion_usuario=int(input("Ingrese una ocpcion:\n1. Piedra.\n2. Papel. \n3. Tijera\n"))
    opcion_maquina =randint(1,3)

    print("Opcion de Usuario:",Texto(opcion_usuario),"\nOpcion de maquina:",Texto(opcion_maquina))
    if(opcion_usuario==1 and opcion_maquina==3)or(opcion_usuario==2 and opcion_maquina==1)or(opcion_usuario==3 and opcion_maquina==2):
        print("******Gana Usuario********")
        gana_usuario+=1
    elif opcion_usuario==opcion_maquina:
        print("********Empate********")
    else:
        print("*****Gana Maquina******")
        gana_maquina+=1
    print()

print("------------Gana usuario-----------") if gana_usuario==3 else print("-------Gana Maquina--------")
print("Fin de Juego")