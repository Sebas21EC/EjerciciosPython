frase="Sebastian Carlosama"
letra="a"
contador=0
for carcater in frase:
    contador+= 1 if carcater==letra else 0

print("La letra se encontró",contador,"veces")  if contador>0 else print("No se encontró la letra")