lista_peso=[50,55,80,75]
suma_mayor=0;
suma_anterior=0;
for i in range(len(lista_peso)):
    for j in range(len(lista_peso)):
        if i!=j and i<j:
            if lista_peso[i]+lista_peso[j]<150:
                print("La suma de",lista_peso[i],"+",lista_peso[j],"=",(lista_peso[i]+lista_peso[j]))
                suma_anterior=lista_peso[i]+lista_peso[j]
                if suma_anterior>suma_mayor:
                    suma_mayor=suma_anterior
                    
print("La suma mayor econtrada es",suma_mayor)