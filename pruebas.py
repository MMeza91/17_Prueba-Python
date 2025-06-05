import random
print(int(1/2))
opcion_niveles = [1, 2, 3]
numero_opciones = opcion_niveles
print(numero_opciones)
    # escoger una pregunta
numero = random.choice(numero_opciones)
    # eliminarla del ambiente global para no escogerla de nuevo
numero_opciones.remove(numero)    
print(numero_opciones)  
print(numero)
print(dir(numero_opciones))


#Borrar antes de entregar programa