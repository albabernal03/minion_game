# minion_game
Mi dirección de Githup para este repositorio es el [siguiente](https://github.com/albabernal03/minion_game)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
En esta tarea hemos resuelto un juego en el que hay dos jugadores (Kevin y Stuart). Stuart tiene que formar palabras que comience por consonantes y Kevin con vocales, el juego termina cuando ambos jugadores hayan creado todas las subcadenas posibles.

Asimismo mencionar que cada jugador recibe un punto por cada vez que la subcadena aparezca en la cadena.

**EJEMPLO VISUAL DEL JUEGO:**


![foto](https://user-images.githubusercontent.com/91721875/145980432-3df10a44-0a9f-481f-9b7d-49a750079de6.jpg)

```
def minion_game(palabra):
    puntuacion_Kevin = 0
    puntuacion_Stuart = 0
    vocales = 'AEIOU'
    s = palabra.upper()

    for i in range (len(s)):
        if s[i] not in vocales:
            puntuacion_Stuart = puntuacion_Stuart + (len(s)-i)
        else:
            puntuacion_Kevin = puntuacion_Kevin + (len(s)-i)
    if puntuacion_Stuart > puntuacion_Kevin:
        print('Stuart es el ganador, con una puntuación =', puntuacion_Stuart)
    elif puntuacion_Stuart < puntuacion_Kevin:
        print('Kevin es el ganador, con una puntuación =', puntuacion_Kevin)
    else:
        print('Kevin y Stuart han empatado')

  

if __name__ == '__main__':
    palabra = input('Elige una palabra:')
    print('La palabra seleccionada es:', palabra)
    minion_game(palabra)
  
```
