
def Imprimir(dicicionario):
    for indice in dicicionario:
        print("Codigo:",indice,"Alumno:",dicicionario[indice])

def AgregarEstudiante(dic,codigo,nombre):
    dic[codigo]=[]
    dic[codigo].append(nombre)
    dic[codigo].append([])

def AgregarNota(dic,codigo,nota):
    dic[codigo][1]+=[nota]

def Promedio(lista):
    suma=0
    for item in lista:
        suma+=item
    return suma/len(lista)

dic ={}
AgregarEstudiante(dic,"001","Sebas")
AgregarNota(dic,"001",10)
AgregarNota(dic,"001",8)
Imprimir(dic)
print(Promedio(dic["001"][1]))