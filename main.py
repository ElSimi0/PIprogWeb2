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


while True:
    print("""
          JUEGOS: Chistes, Dragones, Numero, Ahorcados
          SALIR: x
          """)
    opcion = str(input("¿Que juego te interesa?: ")).lower()
    
    if opcion == "chiste" or opcion == "chistes":
        print("\nEs un juego donde encontraras chistes\ndesde los mas familiares hasta unas\njoyitas escondidas")
        while True:
            iniciar = str(input("Desea Jugar este Juego (y/n) ?: ")).lower()
            if iniciar == "si" or iniciar == "y":
                chistes.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print("No te entendi ni vrga\n")            
    elif opcion == "dragon" or opcion == "dragones":
        print("\nRPG lineal sobre un calabozo, una gran\nhistoria y graficos excelentes (No tiene graficos)")
        while True:
            iniciar = str(input("Desea Jugar este Juego (y/n) ?: ")).lower()
            if iniciar == "si" or iniciar == "y":
                dragones.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print("No te entendi ni vrga\n")              
    elif opcion == "ahorcados" or opcion == "ahorcado":
        print("\nBasado en el manga original, este juego explora\nla cualidad humana bajo el ojo de la naturaleza")
        while True:
            iniciar = str(input("Desea Jugar este Juego (y/n) ?: ")).lower()
            if iniciar == "si" or iniciar == "y":
                ahorcados.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print("No te entendi ni vrga\n")
    elif opcion == "numero" or opcion == "numeros":
        print("numeros :)")
        while True:
            iniciar = str(input("Desea Jugar este Juego (y/n) ?: ")).lower()
            if iniciar == "si" or iniciar == "y":
                adivinaNumero.jugar()
                break
            elif iniciar == "no" or iniciar == "n":
                break
            else:
                print("No te entendi ni vrga\n")
    elif opcion == "ninguno" or opcion == "x" or opcion == "salir":
        break
    else:
        print("No entendi")
                
