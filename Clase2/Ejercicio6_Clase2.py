sexo ="m"
edad=59
cotizaciones=800
anios_servicios=26
if (anios_servicios>=25 and cotizaciones>=750) and ((sexo=="m" and edad >=60)or(sexo=="f" and edad>=55)):
        print("Usted aplica para ser jubilado")
else:
    print("Usted no aplica para ser jubilado")