anio_inicio=2000
anio_fin=2022
resultado= "Los anios bisiestos entre "+str(anio_inicio)+" y "+str(anio_fin)+" son:\n"
for i in range(anio_inicio, anio_fin):
   resultado+=str(i)+"\n" if ((i%4==0 and i%100!=0) or i%400==0) else ""

print(resultado)
