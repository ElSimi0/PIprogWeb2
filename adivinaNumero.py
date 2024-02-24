# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:27:22 2024

@author: sameg
"""
import random

azul = "\033[1;34m"
amarillo = "\033[1;33m"
blanco = "\033[0m"
morado = "\033[1;35m"
rojo = "\033[1;31m"
verde = "\033[1;32m"

def jugar():
    while True:
        intentos = 0
        num = random.randint(0, 100)
        print(verde + "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
        print(verde + "#=#=#=#=💯0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ Adivina el número5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 💯=#=#=#=#")
        print(verde + "#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
      
        print(azul + "Hola y bienvenido al juego Adivina el número ")
        nombre = input(amarillo + "¿Cómo te llamas? ")
        print(blanco + "Mucho gusto ", nombre)
        print(morado + "Las reglas son las siguientes: Vas a tener qué adivinar un número del 0 al 100")
        print("tendrás 10 intentos para hacerlo y para ayudarte en el proceso, la máquina te dirá si es mayor o menor")
        print("Ganarás si aciertas el número antes de los 5 intentos, por el contrario, vas a perder ")
    
        while True:
            try:
                guess = int(input(azul + "Adivina el número: "))
                if 0 <= guess <= 100:
                    intentos += 1
                    if guess == num:
                        print("¡¡¡Victoria ", nombre, "!!!")
                        print(blanco + "Numero de intentos:", intentos)
                        break
                    elif guess < num:
                        print(verde + "El número es mayor")
                    elif guess > num:
                        print(verde + "El número es menor")
                    if intentos == 10:
                        print("Molto male ", nombre)
                        break
                else:
                    print(rojo + "Por favor, ingresa un número válido del 0 al 100.")
            except ValueError:
                print(rojo + "Por favor, ingresa un número válido del 0 al 100.")
    
        jugar_nuevamente = input("¿Deseas jugar de nuevo? (si/no): ")
        if jugar_nuevamente.lower() != 'si':
            break

