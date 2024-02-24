# -*- coding: utf-8 -*-
"""

Created on Sun Feb 18 21:22:37 2024

@author: sameg
"""
#!/usr/bin/env python3

#python C:\Users\sameg\Documents\AIprogWeb\JUEGOS\main.py

import chistes
import dragones
import ahorcados
import adivinaNumero

azul = "\033[1;34m"
amarillo = "\033[1;33m"
blanco = "\033[0m"
morado = "\033[1;35m"
rojo = "\033[1;31m"
verde = "\033[1;32m"

while True:
    print(blanco + """
          JUEGOS: Chistes, Dragones, Numero, Ahorcados
          SALIR: x
          """)
    opcion = str(input(azul + "¿Que juego te interesa?: "+ blanco)).lower()
    
    if opcion == "chiste" or opcion == "chistes":
        print(verde + "\nEs un juego donde encontraras chistes\ndesde los mas familiares hasta unas\njoyitas escondidas\n\n")
        while True:
            iniciar = str(input(azul + "Desea Jugar este Juego (y/n) ?: " + blanco)).lower()
            if iniciar == "si" or iniciar == "y":
                chistes.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print(rojo + "No te entendi ni vrga\n")            
    elif opcion == "dragon" or opcion == "dragones":
        print(morado + "\nRPG lineal sobre un calabozo, una gran\nhistoria y graficos excelentes (No tiene graficos)\n")
        while True:
            iniciar = str(input(azul + "Desea Jugar este Juego (y/n) ?: "+ blanco)).lower()
            if iniciar == "si" or iniciar == "y":
                dragones.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print(rojo + "No te entendi ni vrga\n")              
    elif opcion == "ahorcados" or opcion == "ahorcado":
        print(verde + "\nBasado en el manga original, este juego explora\nla cualidad humana bajo el ojo de la naturaleza\n")
        while True:
            iniciar = str(input(azul + "Desea Jugar este Juego (y/n) ?: " + blanco)).lower()
            if iniciar == "si" or iniciar == "y":
                ahorcados.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print(rojo + "No te entendi ni vrga\n")
    elif opcion == "numero" or opcion == "numeros":
        print(morado + "\nnumeros :)\n")
        while True:
            iniciar = str(input(azul + "Desea Jugar este Juego (y/n) ?: ")).lower()
            if iniciar == "si" or iniciar == "y":
                adivinaNumero.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print(rojo + "No te entendi ni vrga\n")
    elif opcion == "ninguno" or opcion == "x" or opcion == "salir":
        break
    else:
        print(rojo + "No entendi")
                
