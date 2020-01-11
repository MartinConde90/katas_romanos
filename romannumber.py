class RomanNumber():
    __valores = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    __valores_5 = {'V': 5,'L': 50,'D': 500}
    __simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    __rangos = {
        0: {1: 'I', 5: 'V', 'next': 'X'},
        1: {1: 'X', 5: 'L', 'next': 'C'},
        2: {1: 'C', 5: 'D', 'next': 'M'},
        3: {1: 'M', 'next': 'X'},
    }

    def __init__(self,value): #value es el dato que viene de fuera, el numero en humano
        self.value = value    #pero queremos hacerlo propio de esta funcion, asi que lo llamamos y le damos el valor
        self.__romanvalue = self.__arabigo_a_romano() #no ponemos nada dentro del parametro, porque ya está como atributo *value*
                                                  #de aqui sale el numero en romano

    def __invertir(self,cad):
        return cad[::-1] #para darle la vuelta a la cifra
        
    def __gruposDeMil(self): #no hay que informarle nada porque(abajo), todos las funciones sirven a la clase
        cad = str(self.value)#esto ya es self.value
        dac = self.__invertir(cad)
        grupos = []
        rango = 0

        for i in range(0, len(cad), 3): #desde 0 hasta len, de 3 en 3
            grupos.append([rango, int(self.__invertir(dac[i:i+3]))]) # hacemos otro invertir para poner los numeros al derecho
            rango += 1 #el rango son los parentesis, al leer el numero desde atras, vamos aumentando en 1 en cada grupo

        for i in range(len(grupos)-1): # restamos uno a la longitud para tener el numero real de item segun python
                grupoMenor = grupos[i] # grupo del que partimos
                grupoMayor = grupos[i+1] # grupo siguiente con el que comparamos
                unidadesMayor = grupoMayor[1] % 10 # si el resto de la posicion 1 del grupo (el numero, la 0 es el rango)
                                                #  da 4 o mas, se queda donde está
                if unidadesMayor < 4:              #si el resto da menor de 4, pertenece a los millares del grupo anterior
                    grupoMenor[1] = grupoMenor[1] + unidadesMayor * 1000 # añadimos al grupo anterior, las unidades del mayor, por mil
                    grupoMayor[1] = grupoMayor[1] - unidadesMayor    #al grupo mayor le quitamos sus unidades

        grupos.reverse()
        return grupos

    def __arabigo_individual(self,valor): #aqui informamos *valor*, porque no es un atributo de la clase, no es general
        cad = self.__invertir(str(valor))
        res = ''

        for i in range(len(cad)-1,-1,-1): #con el numero invertido, comenzamos por el final, asi sabemos su longitud y que unidad es
            digit = int(cad[i])
            if digit <= 3:
                res += digit*self.__rangos[i][1] #el numero, multip por el simbolo romano que hay en ese rango y en esa posicion
            elif digit == 4:
                res += (self.__rangos[i][1]+self.__rangos[i][5]) #rangos se llama porque es propia de la clase
            elif digit == 5:
                res += self.__rangos [i][5]
            elif digit <9:
                res += (self.__rangos[i][5]+self.__rangos[i][1]*(digit-5))
            else:
                res += self.__rangos[i][1]+self.__rangos[i]['next']

        return res

    def __arabigo_a_romano(self): #aqui no ponemos valor, porque si que es el de la clase
        g1000 = self.__gruposDeMil()
        romanoGlobal = ''

        for grupo in g1000:
            rango = grupo[0]
            numero = grupo[1]
            if numero > 0:
                miRomano = '(' * rango + self.__arabigo_individual(numero) + ')'*rango
            else: 
                miRomano = ''
            romanoGlobal += miRomano

        return romanoGlobal

    def __str__(self):
        return (self.__romanvalue)

    def __repr__(self):
        return self.__romanValue
    
    def __add__(self, value):
        #esto no funcionará
        return RomanNumber(value) + self.value