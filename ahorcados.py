# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:26:49 2024

@author: sameg
"""
import random

azul = "\033[1;34m"
amarillo = "\033[1;33m"
blanco = "\033[0m"
morado = "\033[1;35m"
rojo = "\033[1;31m"
verde = "\033[1;32m"

IMÁGENES_AHORCADO = ['''

     +---+
     |   |
         |
         |
         |
         |
  =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAlAzar(listaDePalabras):
  # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
  índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
  return listaDePalabras[índiceDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
      print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
      print()

      print(rojo + 'Letras incorrectas:', end=' ')
      for letra in letrasIncorrectas:
          print(letra, end=' ')
      print()

      espaciosVacíos = '_' * len(palabraSecreta)

      for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
          if palabraSecreta[i] in letrasCorrectas:
              espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

      for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
          print(verde + letra, end=' ')
      print()

def obtenerIntento(letrasProbadas):
      # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
      while True:
          print(azul + 'Adivina una letra.')
          intento = input()
          intento = intento.lower()
          if len(intento) != 1:
              print(rojo + 'Por favor, introduce una letra.')
          elif intento in letrasProbadas:
              print(rojo + 'Ya has probado esa letra. Elige otra.')
          elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
              print(rojo + 'Por favor ingresa una LETRA.')
          else:
              return intento

def jugarDeNuevo():
     # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
     print(azul + '¿Quieres jugar de nuevo? (sí o no)')
     return input().lower().startswith('s')


def jugar():
    Juego = print(blanco + 'A H O R C A D O')  
    letrasIncorrectas = ''
    letrasCorrectas = ''
    palabraSecreta = obtenerPalabraAlAzar(palabras)
    juegoTerminado = False
    while True:
      mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    
         # Permite al jugador escribir una letra.
      intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    
      if intento in palabraSecreta:
             letrasCorrectas = letrasCorrectas + intento
    
        # Verifica si el jugador ha ganado.
             encontradoTodasLasLetras = True
             for i in range(len(palabraSecreta)):
                 if palabraSecreta[i] not in letrasCorrectas:
                     encontradoTodasLasLetras = False
                     break
             if encontradoTodasLasLetras:
                 print(verde + '¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                 juegoTerminado = True
      else:
             letrasIncorrectas = letrasIncorrectas + intento
    
             # Comprobar si el jugador ha agotado sus intentos y ha perdido.
             if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
                 mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
                 print(amarillo + '¡Te has quedado sin intentos!\nDespués de ' + blanco+ str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
                 juegoTerminado = True
    
         # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
      if juegoTerminado:
             if jugarDeNuevo():
                 letrasIncorrectas = ''
                 letrasCorrectas = ''
                 juegoTerminado = False
                 palabraSecreta = obtenerPalabraAlAzar(palabras)
             else:
                break
if __name__ == "__main__":
    jugar()
else:
    pass