lista_1=["a", "b", "c", "d", "e"]
lista_2=["c", "e", "f","t","g"]
lista_todo=[]
lista_solo_1=[]
lista_solo_2=[]
lista_ambas=[]
lista_todo=lista_1+lista_2

for palabra in lista_1:
    if palabra in lista_2:
        lista_ambas+=[palabra]
    else:
        lista_solo_1+=[palabra]

for palabra in lista_2:
    if palabra not in lista_ambas:
        lista_solo_2+=[palabra]

print(lista_todo)
print(lista_ambas)
print(lista_solo_1)
print(lista_solo_2)