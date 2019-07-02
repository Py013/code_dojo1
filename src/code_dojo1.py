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


def verifica_primos(num):
    count = 0 
    for i in range(1, num+1):  
        if (num % i) == 0:  
            count += 1  
    return count == 2  

# 
def fatores_primos(num):
    fatores = []  
    i = 2 
    if int(num) <= 1 or type(num) is str: 
        return fatores
    while i < num+1: 
        if verifica_primos(i) and num % i == 0:  
            fatores.append(i)  
            num = num/i 
            i = 2 
            continue 
        i += 1 
    return fatores 

#
# def testa_programa():
#     num = int(input("Digite o numero a ser fatorado: "))
#     print(fatores_primos(num))
#     pass

# testa_programa()
'''
verifica_primos(num)
linha | Explicação
1       Função que verifica se um numero eh primo, retornando um boolean
2       Cria um contador
3       Faz um looping de intervalo [1,num+1]
4       Esse If foi feito para averiguar a quantidade de divisores que 'num' tem. Para ser primo 'num' deve ter apenas dois divisores - 1 e 'num' - caso contrário não será classificado dessa forma
5       count irá incrementar de acordo com a quantidade de divisores que num possuir
7       Se count for igual a dois significa que 'num' é primo, pois só é divisível por um e ele mesmo, logo a função retorna True, caso contrário retornará False
fatores_primos(num)
1       Função criada para verificar todos os fatores primos que formam um número 'num'
2       Criamos uma lista vazia, esta armazenará os fatores primos
3       Essa variável será utilizada no looping, começa em dois pois esse é o menor número primo disponível.
4       verifica se o número passado é menor ou igual a 1, ou se ele é na verdade uma String. Nesses casos, retorna-se uma lista vazia uma vez que não é possível fatorar      
5       A laço while é criado para realizar o looping no intervalo de [i, num+1]
6       Verifica se o numero da vez é primo e divisor de 'num', nesse caso ele também será um fator de 'num'
7       Por ser fator de 'num', 'i' é incluído na lista criada anteriormente 
8       O valor de num é atualizado, sendo dividido por seu fator primo encontrado para que possa ser fatorado novamente na próxima iteração
9       O valor de 'i' volta a ser 2 porque cada fatoração precisa ser feita com o menor numero primo que também é divisor do número a ser fatorado
10      Nesse caso, seguimos para o próximo looping uma vez que conseguimos encontrar um dos fatores primos de 'num'
11      Caso não for possível encontrar um dos fatores primos de num nessa iteração, incrementamos 'i' e seguimos para a próxima
12      Retornamos a lista de fatores ao final do processo
'''


'''
Desafio3: Jokenpo
Enunciado em: http://dojopuzzles.com/problemas/exibe/jokenpo/
'''