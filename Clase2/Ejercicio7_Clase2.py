from random import randint
zona_usuario=3
print("Zona disparada:",zona_usuario)
zona_portero= randint(1,6)
print("Zona cubierta por el portero:",zona_portero)
print("No gol") if int(zona_usuario)==int(zona_portero) else print("Gol")
