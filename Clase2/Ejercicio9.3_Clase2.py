hora =22
minutos=8
segundo =57

if(hora<24 or minutos<60 or segundo<60):
    segundo+=1
    if segundo==60:
        minutos+=1
        segundo=0
        if minutos==60:
            hora+=1
            minutos=0
            if hora==24:
                hora=0
    print("La hora un segundo despues es:",hora,"",minutos,"",segundo)
else:
    print("La hora ingresada es incorrecta")