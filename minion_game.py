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
  