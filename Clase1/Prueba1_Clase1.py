import datetime;

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
full_name=nombre+" "+apellido
anio_nacimiento=int(input("Ingrese su año de nacimiento: "))
date = datetime.date.today()
anio_actual = date.strftime("%Y")
edad =int(anio_actual)-anio_nacimiento
print("Nombre completo:",full_name)
print("Edad: ",edad)
