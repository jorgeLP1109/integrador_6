import os
import time
from functools import reduce

def convertir_mapa(mapa_str):
    return list(map(list, mapa_str.strip().split("\n")))

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    limpiar_pantalla()
    print('\n'.join(''.join(fila) for fila in mapa))

def main_loop(mapa, inicio, final):
    px, py = inicio
    fx, fy = final
    
    while (px, py) != (fx, fy):
        mostrar_mapa(mapa)
        tecla = input("Introduce una dirección (w/a/s/d): ")
        
        if tecla == 'w':
            nx, ny = px - 1, py
        elif tecla == 's':
            nx, ny = px + 1, py
        elif tecla == 'a':
            nx, ny = px, py - 1
        elif tecla == 'd':
            nx, ny = px, py + 1
        else:
            continue
        
        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and mapa[nx][ny] != '#':
            mapa[px][py] = '.'
            px, py = nx, ny
            mapa[px][py] = 'P'

# Coordenadas iniciales y finales
mapa_str = """
..#########
..........#
#.###.#####
#.#.#.#...#
#.#.#####.#
#.........#
###.###.#.#
#.....#.#.#
#####.###.#
#.......#.
#######...
"""

inicio = (0, 0)
final = (5, 5)  #  coordenadas dentro de los límites del mapa

mapa = convertir_mapa(mapa_str)

if (0 <= inicio[0] < len(mapa) and 0 <= inicio[1] < len(mapa[0]) and
    0 <= final[0] < len(mapa) and 0 <= final[1] < len(mapa[0])):
    main_loop(mapa, inicio, final)
else:
    print("Las coordenadas de inicio o final están fuera del rango del mapa.")
