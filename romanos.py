valores = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano:
        if letra == ultimoCaracter:
            numRepes +=1
        else:
            numRepes = 1
        
        if numRepes > 3:
            return 0

        if letra in valores:
            numArabigo += valores[letra]
        else:
            return 0

        ultimoCaracter = letra

    return numArabigo