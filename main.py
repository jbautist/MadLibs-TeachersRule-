import os
import historias as h


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


print('''
                        +--------------------------+
                        | MAD LIBS: Teachers Rule! |
                        +--------------------------+

Esta es una adaptación al español del libro Mad Libs, edición: "Teachers Rule!"

                               INSTRUCCIONES
Complete las palabras que se le vayan solicitando para generar la historia.
''')
ENTER = input('\nPresione ENTER para continuar.')

clearConsole()

seguir_jugando = 'S'

while seguir_jugando == 'S':
    print('''\nElige una historia

    [1] ¡EL PERRO SE LO COMIÓ!
    [2] LAS MEJORES COSAS DE SER MAESTRO
    [3] REGALOS PARA PROFESORES
    [4] TIPOS DE PROFESORES
    [5] DETRÁS DE ESCENAS: EL SALÓN DE PROFESORES 
    [6] LAS VIDAS SECRETAS DE LOS PROFESORES
    [7] CÓMO CONVERTIRSE EN MAESTRO
    [8] UN DÍA EN LA VIDA DE UN MAESTRO
    [9] CÓMO CONVERTIRSE EN LA MASCOTA DEL PROFESOR

    [10] Salir
    ''')

    seleccion = input()

    clearConsole()

    if seleccion == '1':
        h.historia_1()
    elif seleccion == '2':
        h.historia_2()
    elif seleccion == '3':
        h.historia_3()
    elif seleccion == '4':
        h.historia_4()
    elif seleccion == '5':
        h.historia_5()
    elif seleccion == '6':
        h.historia_6()
    elif seleccion == '7':
        h.historia_7()
    elif seleccion == '8':
        h.historia_8()
    elif seleccion == '9':
        h.historia_9()
    elif seleccion == '10':
        exit()
    else:
        print('\nERROR: has ingresado un carácter o número incorrecto. Por favor elige una historia del [1] al [9] o ingresa [10] para salir.')
        continue

    # Bucle para comprobar que el usuario ingrese 's, n, S o N.
    while True:  
        seguir_jugando = input('\n¿Quiere seguir jugando? [S/N] ')
        if not seguir_jugando.isalpha():
            print('\nError: has ingresado un caracter incorrecto.')
        elif seguir_jugando.upper() == 'S' or seguir_jugando.upper() == 'N':
            break
        else:
            print('\nError: has ingresado una letra incorrecta.')

    seguir_jugando = seguir_jugando.upper()
    clearConsole()