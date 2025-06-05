
# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# valores iniciales - 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'
opciones_trivia = ['0', '1']
opciones_niveles = ['1', '2', '3']  #Se crean variables con lista de opciones para funciones posteriores
opciones_alternativa = ['a','b','c','d']
opciones_continuar = ['y','n']

# ----------------------------------------

os.system(op_sys) # limpiar pantalla

print('Bienvenido a la Trivia')

# Se crea while para repetir pregunta en caso de que validate entregue False
validado = False
while not validado:
    opcion = input('''Ingrese una opción para Jugar!
            1. Jugar
            0. Salir
            
        > ''')
    # 1. validar opcion
    validado = validate(opciones_trivia,opcion)

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print("Nos vemos en una próxima ocación")
    time.sleep(2)
    os.system(op_sys)
    correcto = False
    # finalizar programa
    

# Funcionamiento de preguntas
while correcto and n_pregunta < 3*p_level:
    
    if n_pregunta == 0:

        #Se realiza un bucle para asegurar que respuesta esté dentro de las opciones
        validado = False
        while not validado:
            p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
            # 3. Validar el número de preguntas por nivel

            validado = validate(opciones_niveles,p_level)
        p_level = int(p_level)
        
    if continuar == 'y':
        #contador de preguntas
        n_pregunta += 1
        # 4. Escoger el nivel de la pregunta
        nivel = choose_level(n_pregunta,p_level)
        print(f'Pregunta {n_pregunta}:')


        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        
        enunciado, alternativas = choose_q(nivel)
        #6. Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado,alternativas)
        

        # 7. Validar la respuesta entregada
        #Se realiza un bucle para asegurar que respuesta esté dentro de las opciones
        validado = False
        while not validado:
            respuesta = input('Escoja la alternativa correcta:\n> ').lower()
            validado = validate(opciones_alternativa,respuesta)

        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas,respuesta)
        
        if correcto and n_pregunta < 3*p_level:
            print('\nMuy bien sigue así!')
            
            #Se realiza un bucle para asegurar que respuesta esté dentro de las opciones
            valido = False
            while not valido:
                continuar = input('\nDesea continuar? [y/n]: ').lower()
                #9. Validar si es que se responde y o n
                valido = validate(opciones_continuar,continuar)


            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(4)
            os.system(op_sys)
        else: 
            print(f'\nLo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(4)
            exit()
    else: 
        print('\nNos vemos la proxima vez, sigue practicando')
        time.sleep(4)
        exit()
            
            
