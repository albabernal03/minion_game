def minion_game(palabra):
    puntuacion_Kevin = 0
    puntuacion_Stuart = 0
    vocales = 'AEIOU'
    s = palabra.upper()

    for i in range (len(s)):
        if s[i] not in vocales:

  

if __name__ == '__main__':
    palabra = input('Elige una palabra:')
    minion_game(palabra)