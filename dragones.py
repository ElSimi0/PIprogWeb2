# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:26:28 2024

@author: sameg
"""
import random
import time




def mostrarIntroduccion():
    print("Estás en busca de un tesoro dentro de una tierra llena de dragones. Frente a ti hay dos cuevas. En una de ellas, el dragón es generoso y amigable y compartirá su tesoro contigo. El otro dragón es codicioso y está hambriento, y te devorará inmediatamente.")

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()
    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un gran dragón aparece súbitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('\033[45;3m''¡Te regala su tesoro!')
    else:
        print('¡Te come de un bocado!')


def jugar():
    jugarDeNuevo = 'si'
    while jugarDeNuevo == 'si' or jugarDeNuevo == 's':
        mostrarIntroduccion()
        númeroDeCueva = elegirCueva()
        explorarCueva(númeroDeCueva)
        print('¿Quieres jugar de nuevo? (si o no)')
        jugarDeNuevo = input().lower()
