# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:23:32 2024

@author: sameg
"""
import time
import random as rd

azul = "\033[1;34m"
amarillo = "\033[1;33m"
blanco = "\033[0m"
morado = "\033[1;35m"
rojo = "\033[1;31m"
verde = "\033[1;32m"

password = "222559028"
cl = 31
speed = 0.1

def chistes(tipo):
    chistes = {
        "blanco" : [
            """
            ¿Que le Dijo Un Semaforo A Otro Semaforo?
            -¡No mires me estoy cambiando!.
            """,
            """
            ¿Por que el CD no funciona?
            -Porque CDscompuso.
            """,
            """
            ¿Cual es el deseo de una servilleta?
            -Ser Billete.
            """,
            """
            ¿Que Planeta Va Despues De Marte?
            -Miercole.
            """,
            """
            ¿Que Dijo La Cereza Al Verse En El Espejo?
            -Cere_eza?.
            """
            ],
        
        "gris" : [
            """
            Nunca le rompas el corazón a alguien solo tienen uno,
            -Rómpele los huesos mejor, tienen 206.
            """,
            """
            Acabo de leer que en Nueva York alguien es apuñalado cada 52 segundos,
            -Pobre tipo.
            """,
            """
            ¿Qué es rojo y malo para los dientes?
            -Un Ladrillo.
            """,
            """
            'Papá, ¿ya tienes los resultados de la prueba de ADN?'
            -'Llámame Andrés.'
            """,
            """
            Estaba en Rusia escuchando a un cómico burlándose de Putin, 
            Los chistes no eran tan buenos,
            -pero la ejecución fue de primera.
            """
            ],
        "negro" : [
            """
            ¿Sabes como matar 250 moscas de un solo golpe?
            -Pateando a un niño somali.
            """,
            """
            ¿En que se parece un niño con cancer y una 
            iglesia abandonada?
            -Ninguno tiene cura.
            """,
            """
            ¿Qué tiene dos patas y sangra mucho? 
            -Medio perro.
            """,
            """
            ¿En donde quedo la niña despues del bombardeo?
            -En todas partes.
            """,
            """
            ¿Que hace una niña arabe en un columpio?
            -Marear al francotirador.
            """
            ],
        "insano" : [
            """
            ¿Cual es la diferencia entre Einsten y el bebe que acabo de matar?
            -Einsten murio Virgen….
            """,
            """
            Van 2 negros en un carro uno con gorra y el otro sin gorra ¿cuál maneja?
            -El Policia.
            """,
            """
            ¿Qué es un cura en una guarderia? 
            -Despedida de soltero.
            """,
            """
            ¿Que es negro, rojo, tiene 4 brazos y dos cabezas?
            -Un Rottweiler en un kinder.
            """,
            """
            'Te cambio una de 10 por dos de 5'
            -Conversacion entre curas.
            """
            ]
        }
    return rd.choice(chistes.get(tipo, chistes["blanco"]))

def jugar():
    continuar = True
    while continuar == True:
        while True:
            tipo = str(input(blanco+"\nQue tipo de chiste quieres \nBlanco, Gris, Negro o Insano : ")).lower()
            if tipo == "blanco" or tipo == "gris":
                chiste = chistes(tipo).title()
                break
            elif tipo == "negro" or tipo == "insano":
                contra = str(input(rojo + "\nDebido a obvias razones \nes necesaria una contraseña: "+blanco))
                if contra == password:
                    chiste = chistes(tipo).title()
                    break
                else:
                    print(verde + "Contraseña es incorrecta\n" + blanco)
            elif tipo != "blanco" or tipo != "gris" or tipo != "negro" or tipo != "insano":
                time.sleep(0.3)
                print(rojo+"\nERROR: Escribe bien xfa\n"+blanco)
                time.sleep(0.1)
        speed = 0.1
        
        for letra in chiste:
            print(blanco + letra, end='', flush=True)
            if letra == "-":
                speed = 0.15
            elif letra == ".":
                speed = 0.1
            time.sleep(speed)
        while True:
            ask = str(input(azul + "\nDesea Continuar (y/n) ? : ")).lower()
            if ask == "y" or ask == "si" or ask == "yes":
                break
            elif ask == "n" or ask == "no":
                continuar = False
                break
            else:
                print(rojo + "\nDisculpa no entendi bien (Escribe bien)\n")
                pass
                
if __name__ == "__main__":
    jugar()
else:
    pass
