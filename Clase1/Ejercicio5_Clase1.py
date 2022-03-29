correctos=int(input("Ingrese el numero de aciertos: "))
errores=int(input("Ingrese el numero de errores: "))
total = correctos+errores
porc_correcto=(100/total)*correctos
porc_errores=(100/total)*errores
print("Su puntaje final fue:",str(correctos),"/",str(total))
print("Su porcentaje de aciertos es: %.2f y un porcentaje de errores de: %.2f"%(porc_correcto,porc_errores))
