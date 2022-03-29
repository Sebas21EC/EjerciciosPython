jornada=48
h_trabajadas=49
pago_hora=2
pago_hora_extra=3.5
sueldo = sueldo=(jornada*pago_hora)+((h_trabajadas-jornada)*pago_hora_extra) if h_trabajadas>jornada else h_trabajadas*pago_hora
print("Su salario es de:",sueldo)