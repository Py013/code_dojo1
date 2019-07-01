'''
Py013 - Code dojo 29/09/2016

Desafio1: ano_bissexto
Enunciado em: http://dojopuzzles.com/problemas/exibe/ano-bissexto/

Um determinado ano é bissexto se:
O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.
'''

def divisivel(dividendo, divisor):
    return not dividendo % divisor

def ano_bissexto(ano):
    if not divisivel(ano, 4):
        return False

    if divisivel(ano, 400):
        return True

    return not divisivel(ano, 100)

'''
Desafio2: fatores primos
Enunciado em: http://dojopuzzles.com/problemas/exibe/geracao-de-fatores-primos/
'''
def verifica_primos(numero):
    count = 0
    for x in range(1, numero+1):
        if (numero % (x) == 0):
            count += 1
        if count > 2:
            return False

    return True



def fatores_primos(numero):
    resultado = numero
    fatores = []
    #if verifica_primos(numero):
        #resultado = numero
        #fatores = []
    'for x in range(numero, reverse = true): Possível aplicabilidade mas eu n soube utilizar o reverse'
    #while not verifica_primos(resultado):
    for x in range(2, numero):
        if (resultado % x == 0)):

        resultado = int(resultado / x)
        fatores.append(x)



    #if count > 2:
    #    return False


    return fatores

'''
Desafio3: Jokenpo
Enunciado em: http://dojopuzzles.com/problemas/exibe/jokenpo/
'''