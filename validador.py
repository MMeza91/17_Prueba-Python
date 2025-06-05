
def validate(opciones:list[str], eleccion):
    # Definir validación de eleccion
    ##########################################################################

    if eleccion in opciones:
        duda = True
    else: 
        print('Opción no válida, ingrese una de las opciones válidas: ')
        duda = False
    ##########################################################################
    return duda


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
    sin_respuesta = False
    while not sin_respuesta:
        opcion = input('''Ingrese una opción para Jugar!
                1. Jugar
                0. Salir
                
            > ''')
        # 1. validar opcion
        sin_respuesta = validate(numeros,opcion)