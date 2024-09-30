from Equipos.Barcelona import *
from Equipos.Real_madri import *
from Equipos.bayern import  *
from Equipos.city import *
from Equipos.inter import *
from Equipos.Liverpool import *
from Equipos.milan import *
from Equipos.psg import *

def elegir_equipo(jugador: str) -> dict:
    
    while True:
        try:
            print (f"| 1: Barcelona |\n| 2 : Real Madrid |\n| 3 : Bayern  |\n| 4 : City  |\n| 5 : Inter  |\n| 6 : Liverpool  |\n| 7 : Milan   |\n| 9 :Psg")
            seleccion = int(input(f"{jugador}, ¿Cuál equipo desea escoger?: "))
            if 1 <= seleccion <= 9:
                break
            else:
                print("ERROR, escoja nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    equipo_seleccionado = teams.get(seleccion)
    if equipo_seleccionado:
        print("Escudo del equipo:")
        for linea in equipo_seleccionado["escudo"]:
            print(linea)
    
    jugadores = equipo_seleccionado["jugadores"]
    ataque = equipo_seleccionado["ataque"]
    defensa = equipo_seleccionado["defensa"]
    costo = equipo_seleccionado["costo"]

    return jugadores, ataque, defensa, costo

def elegir_modo_juego() -> int:
    while True:
        try:
            modo = int(input("Escoja un modo de juego (1, 2, 3): "))
            if 1 <= modo <= 3:
                rondas = {1: 9, 2: 12, 3: 15}[modo]
                return rondas
            else:
                print("ERROR, escoja nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def insertar_en_columnas(fila, columna, numero_jugador, columnas):
    if fila_p1 == 1 and columna_p1 == 1:
        columnas_jugador_uno[0].insert(0, numero_jugador_escogido)
    if fila_p1 == 2 and columna_p1 == 1:
        columnas_jugador_uno[0].insert(-1, numero_jugador_escogido)
    if fila_p1 == 1 and columna_p1 == 2:
        columnas_jugador_uno[1].insert(0, numero_jugador_escogido)
    if fila_p1 == 2 and columna_p1 == 2:
        columnas_jugador_uno[1].insert(-1, numero_jugador_escogido)
    if fila_p1 == 1 and columna_p1 == 3:
        columnas_jugador_uno[2].insert(0, numero_jugador_escogido)
    if fila_p1 == 2 and columna_p1 == 3:
        columnas_jugador_uno[2].insert(-1, numero_jugador_escogido)
    if fila_p1 == 1 and columna_p1 == 4:
        columnas_jugador_uno[3].insert(0, numero_jugador_escogido)
    if fila_p1 == 2 and columna_p1 == 4:
        columnas_jugador_uno[3].insert(-1, numero_jugador_escogido)
        
    if fila_p2 == 4 and columna_p2 == 1:
        columnas_jugador_dos[0].insert(0, numero_segundo_escogido)
    if fila_p2 == 5 and columna_p2 == 1:
        columnas_jugador_dos[0].insert(-1, numero_segundo_escogido)
    if fila_p2 == 4 and columna_p2 == 2:
        columnas_jugador_dos[1].insert(0, numero_segundo_escogido)
    if fila_p2 == 5 and columna_p2 == 2:
        columnas_jugador_dos[1].insert(-1, numero_segundo_escogido)
    if fila_p2 == 4 and columna_p2 == 3:
        columnas_jugador_dos[2].insert(0, numero_segundo_escogido)
    if fila_p2 == 5 and columna_p2 == 3:
        columnas_jugador_dos[2].insert(-1, numero_segundo_escogido)
    if fila_p2 == 4 and columna_p2 == 4:
        columnas_jugador_dos[3].insert(0, numero_segundo_escogido)
    if fila_p2 == 5 and columna_p2 == 4:
        columnas_jugador_dos[3].insert(-1, numero_segundo_escogido)
    # Evaluación de las columnas para los goles y las defensas
    
def evaluar_columna(columna, columnas_uno, columnas_dos, goles_p1, goles_p2):
    
    actualizar_matriz : int = 44
    columna_evaluada : int = 0
    while columna_evaluada <= 4:

        if len(columnas_jugador_uno[columna_evaluada]) == 1 and len(columnas_jugador_dos[columna_evaluada]) == 0:
            goles_primer_jugador += ataque_jugadores_p1[numero_jugador_escogido]

        elif len(columnas_jugador_dos[columna_evaluada]) == 1 and len(columnas_jugador_uno) == 0:
            goles_segundo_jugador += ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]

        elif len(columnas_jugador_uno[columna_evaluada]) == 2 and len(columnas_jugador_dos[columna_evaluada]) == 0:
            goles_primer_jugador += ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] + ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]

        elif len(columnas_jugador_dos[columna_evaluada]) == 2 and len(columnas_jugador_uno[columna_evaluada]) == 0:
            goles_segundo_jugador += ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] + ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]

        elif len(columnas_jugador_uno[columna_evaluada]) == 2 and len(columnas_jugador_dos[columna_evaluada]) == 1:
            
            defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]
            if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada] = " " * 100

            defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]
            if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                goles_primer_jugador += ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                for i in range(actualizar_matriz * 2):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100
            else:
                defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

        elif len(columnas_jugador_dos[columna_evaluada]) == 2 and len(columnas_jugador_uno[columna_evaluada]) == 1:
            defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
            if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada] = " " * 100

            defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]
            if defensa_jugadores_p1|[columnas_jugador_uno[columna_evaluada[0]]] <= 0:
                goles_segundo_jugador += ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]
                for i in range(actualizar_matriz * 2):
                    matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100
            else:
                defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]
                if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz * 2):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada] = " " * 100

        elif len(columnas_jugador_uno[columna_evaluada]) == 2 and len(columnas_jugador_dos[columna_evaluada]) == 2:

            defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]]
            defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]]


            if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada]
                defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 4) + i][columna_evaluada]
            elif defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] > 0:
                defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] -= ataque_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]]
                if defensa_jugadores_p2[columnas_jugador_dos[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 3) + i][columna_evaluada]

            elif defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] <= 0:
                for i in range(actualizar_matriz):
                    matriz_visual[(actualizar_matriz) + i][columna_evaluada]
                defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]
                if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[0]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz * 0) + i][columna_evaluada]
            elif defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] > 0:
                defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] -= ataque_jugadores_p2[columnas_jugador_dos[columna_evaluada[1]]]
                if defensa_jugadores_p1[columnas_jugador_uno[columna_evaluada[1]]] <= 0:
                    for i in range(actualizar_matriz):
                        matriz_visual[(actualizar_matriz) + i][columna_evaluada]

        columna_evaluada += 1

    return goles_p1, goles_p2
# Bucle de juego por rondas
if __name__ == "__main__":
    
    teams = {
        1: barcelona,
        2: real_madrid,
        3: bayern, 
        4: city,
        5: inter,
        6: liverpool,
        7: milan,
        8: psg
    }

    jugadores_p1, ataque_jugadores_p1, defensa_jugadores_p1, costo_jugadores_p1 = elegir_equipo("Jugador 1")
    jugadores_p2, ataque_jugadores_p2, defensa_jugadores_p2, costo_jugadores_p2 = elegir_equipo("Jugador 2")
    rondas_totales = elegir_modo_juego()

    talentos_jugador_1 : int = 1
    talentos_jugador_2 : int = 1
    matriz_visual = [[" " * 100 for _ in range(5)] for _ in range(226)]

    # Estructuras para almacenar las columnas
    columnas_jugador_uno = [[], [], [], []]
    columnas_jugador_dos = [[], [], [], []]

    # Bucle para evaluar cada columna
    goles_primer_jugador : int = 0
    goles_segundo_jugador : int = 0
    goles_p1 : int = 0
    goles_p2 : int = 0
    ronda = 1
    while ronda <= rondas_totales:
        ronda : int = 1
        print(f"--- Ronda {ronda} ---")
        # Turno del jugador 1
        print("--- Turno del primer jugador ---")
        print(f"-- GOLES P1-- {goles_primer_jugador}")
        print(f"-- GOLES P2-- {goles_segundo_jugador}")
        print(f"-- CREDITOS -- {talentos_jugador_2}")
        numero_jugador_escogido = 100
        while numero_jugador_escogido != 0:
            try:
                numero_jugador_escogido = int(input("Jugador 1, ingresa el dorsal del jugador (0 para continuar): "))
                if numero_jugador_escogido == 0:
                    break
                if numero_jugador_escogido not in jugadores_p1:
                    print("Dorsal inválido, intenta de nuevo.")
                    continue
                
                if talentos_jugador_1 >= costo_jugadores_p1[numero_jugador_escogido]:
                    jugador_escogido = jugadores_p1[numero_jugador_escogido]
                    talentos_jugador_1 -= costo_jugadores_p1[numero_jugador_escogido]
                else:
                    print("No tienes suficientes talentos. Elige otro jugador.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

            # Solicitar fila y columna
            try:
                fila_p1 = int(input("En qué fila (1-2): "))
                while fila_p1 not in [1, 2]:
                    fila_p1 = int(input("ERROR, ingrese una fila válida (1-2): "))

                columna_p1 = int(input("En qué columna (1-4): "))
                while columna_p1 not in [1, 2, 3, 4]:
                    columna_p1 = int(input("ERROR, ingrese una columna válida (1-4): "))
            except ValueError:
                print("Entrada inválida. Deben ser números.")

            filas_p1 = (fila_p1 - 1) * 44

            for i in range(len(jugador_escogido)):
                if filas_p1 + i < len(matriz_visual):
                    matriz_visual[filas_p1 + i][columna_p1] = jugador_escogido[i]

            for r in matriz_visual:
                print("".join(r))

        # Turno del jugador 2
        print("--- Turno del segundo jugador ---")
        print(f"-- GOLES P1-- {goles_primer_jugador}")
        print(f"-- GOLES P2-- {goles_segundo_jugador}")
        print(f"-- CREDITOS -- {talentos_jugador_2}")
        numero_segundo_escogido = 100
        while numero_segundo_escogido != 0:
            try:
                numero_segundo_escogido = int(input("Jugador 2, ingresa el dorsal del jugador (0 para continuar): "))
                if numero_segundo_escogido == 0:
                    break
                if numero_segundo_escogido not in jugadores_p2:
                    print("Dorsal inválido, intenta de nuevo.")
                    continue
                
                if talentos_jugador_2 >= costo_jugadores_p2[numero_segundo_escogido]:
                    segundo_escogido = jugadores_p2[numero_segundo_escogido]
                    talentos_jugador_2 -= costo_jugadores_p2[numero_segundo_escogido]
                else:
                    print("No tienes suficientes talentos. Elige otro jugador.")
                    continue
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

            # Solicitar fila y columna
            try:
                fila_p2 = int(input("En qué fila (4-5): "))
                while fila_p2 not in [4, 5]:
                    fila_p2 = int(input("ERROR, ingrese una fila válida (4-5): "))

                columna_p2 = int(input("En qué columna (1-4): "))
                while columna_p2 not in [1, 2, 3, 4]:
                    columna_p2 = int(input("ERROR, ingrese una columna válida (1-4): "))
            except ValueError:
                print("Entrada inválida. Deben ser números.")

            filas_p2 = (fila_p2 - 1) * 44

            for i in range(len(segundo_escogido)):
                if filas_p2 + i < len(matriz_visual):
                    matriz_visual[filas_p2 + i][columna_p2] = segundo_escogido[i]

            for columna in range(5):
                goles_primer_jugador, goles_segundo_jugador = evaluar_columna(columna, columnas_jugador_uno, columnas_jugador_dos, goles_p1, goles_p2)

            for r in matriz_visual:
                print("".join(r))
    
        ronda += 1
        talentos_jugador_1 += ronda
        talentos_jugador_2 += ronda

    for r in matriz_visual:
        print("".join(r))

