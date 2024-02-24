# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:26:28 2024

@author: valentin
"""
import random
import time

azul = "\033[1;34m"
amarillo = "\033[1;33m"
blanco = "\033[0m"
morado = "\033[1;35m"
rojo = "\033[1;31m"
verde = "\033[1;32m"


def mostrarIntroduccion():
    print("Estás en busca de un tesoro dentro de una tierra llena de dragones. Frente a ti hay dos cuevas. En una de ellas, el dragón es generoso y amigable y compartirá su tesoro contigo. El otro dragón es codicioso y está hambriento, y te devorará inmediatamente.")

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print(azul + '¿A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()
    return cueva

def explorarCueva(cuevaElegida):
    print(blanco + 'Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un gran dragón aparece súbitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print(verde + '¡Te regala su tesoro!')
    else:
        print(rojo + '¡Te come de un bocado!')


def jugar():
    jugarDeNuevo = 'si'
    while jugarDeNuevo == 'si' or jugarDeNuevo == 's':
        mostrarIntroduccion()
        númeroDeCueva = elegirCueva()
        explorarCueva(númeroDeCueva)
        print(azul + '¿Quieres jugar de nuevo? (si o no)')
        jugarDeNuevo = input().lower()
        
if __name__ == "__main__":
    jugar()
else:
    pass
