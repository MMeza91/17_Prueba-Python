import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad


    # usar opciones desde ambiente global
    numero_opciones = opcion_niveles
    # escoger una pregunta
    numero = random.choice(numero_opciones)
    # eliminarla del ambiente global para no escogerla de nuevo
    numero_opciones.remove(numero)
    
    # escoger enunciado y alternativas mezcladas
    pregunta =  p.pool_preguntas[dificultad][f"pregunta_{numero}"]
    alternativas = shuffle_alt(pregunta)
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    opcion_niveles = [1, 2, 3]
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    enunciado, alternativas = choose_q('basicas')
    print(f'El enunciado es: {enunciado}')
    print(f'Las alternativas son: {alternativas}')
    
    enunciado, alternativas = choose_q('basicas')
    print(f'El enunciado es: {enunciado}')
    print(f'Las alternativas son: {alternativas}')
    
    enunciado, alternativas = choose_q('basicas')
    print(f'El enunciado es: {enunciado}')
    print(f'Las alternativas son: {alternativas}')