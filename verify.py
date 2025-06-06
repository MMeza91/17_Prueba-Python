import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada

    eleccion = ['a','b','c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    
    #Se evalua si dentro del diccionario de alternativas la respuesta contiene un 1 que significa respuesta correcta
    if alternativas[eleccion][1] == 1:
        correcto = True
        print('\nRespuesta Correcta')
    else: 
        correcto = False
        print('\nRespuesta Incorrecta')

    
    
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    print(verificar(pregunta['alternativas'], respuesta))






