n=60
x=8

def vaso(n,x):
    total=0
    while(n>=x):
        reciclados = n//x
        sobrantes=n%x
        total+=reciclados
        n=reciclados+sobrantes
        print("N:",n,"Reciclados:",reciclados,"Sobrantes:",sobrantes,"Total reciclados",total)
    return total

vaso(n,x)
