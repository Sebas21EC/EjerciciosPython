from turtle import st


n_dias= int(input("Ingrese numero de dias: "))
anios= n_dias//365
meses=(n_dias%365)//30
semanas=(n_dias-(anios*365+meses*30))//7
dias=n_dias-(anios*365+meses*30+semanas*7)
print("Los",str(n_dias),"dias equivalen a: ",str(anios),"anios,",str(meses),"meses,",str(semanas),"semanas,",str(dias),"dias")