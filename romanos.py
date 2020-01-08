valores = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
valores_5 = {'V': 5,'L': 50,'D': 500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:      
        #incrementamos el valor del numero arabigo con el valor numero del simbolo romano
        if letra in valores:
            numArabigo += valores[letra] #lo ponemos aqui ya que es una variable general

            if ultimoCaracter == '':
                pass

            elif valores[ultimoCaracter] > valores[letra]: #si el numero es menor que el anterior
                numRepes = 1

            elif valores[ultimoCaracter] == valores[letra]: #si hay dos numeros iguales seguidos
                numRepes += 1

                if letra in valores_5 and ultimoCaracter in valores_5: #solo deberiamos comprobar uno, porque en el elif ya dice que son iguales
                    return 0

                if numRepes > 3:
                    return 0

            elif valores[ultimoCaracter] < valores[letra]: #cuando hay 2 numeros menores delante de uno mayor
                if numRepes > 1: #no permite repeticiones en las restas
                    return 0

                if ultimoCaracter in valores_5: #no permite restas de valores de 5 (5, 50, 500)
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de mas de un orden
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter] * 2
                numRepes = 1

        else: #si el simbolo romano no está permitido, devolvemos error (0)
            return 0 

        ultimoCaracter = letra

    return numArabigo

def arabigo_a_romano(valor):
    pass