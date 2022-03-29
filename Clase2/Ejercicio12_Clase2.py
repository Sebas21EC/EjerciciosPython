altura=5
espacios = altura
caracteres=1
for i in range(altura):
    for j in range(espacios):
        print("  ",end="")
    espacios-=1
    for k in range(caracteres):
        print("* ",end="")
    caracteres+=2
    print()

for i in range(altura+1):
    for j in range(espacios):
        print("  ",end="")
    espacios+=1
    for k in range(caracteres):
        print("* ",end="")
    caracteres-=2
    print()

    
