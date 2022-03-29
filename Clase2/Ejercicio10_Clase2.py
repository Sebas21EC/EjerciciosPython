numero = 20
respuesta="El numero " +str(numero) + " es divible para"
#range(inicio, fin, paso)
for i in range(1,(numero//2)+1,1):
     respuesta+=" "+str(i) if numero%i==0 else ""
respuesta+=" "+str(numero)
print(respuesta)