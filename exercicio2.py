#(2) Escreva uma função que receba dois números inteiros como parâmetros, n1 e n2,
#onde n1 precisa ser menor ou igual a n2. A função deverá fazer o seguinte:
#•Se n1 ≤ n2, calcular e retornar a soma dos números ímpares no intervalo que
#começa em n1 e vai até n2.
#o Exemplo1: se o usuário digitar n1 = 3 e n2 = 12, a função deverá calcular
#a soma: 3 + 5 + 7 + 9 + 11, retornando o valor 35.
#o Exemplo2: se o usuário digitar n1 = 31 e n2 = 35, a função deverá
#calcular a soma: 31 + 33 + 35, retornando o valor 99.
#• Se n1 > n2, a função não deverá fazer o cálculo. Em vez disso, retornará o valor
#None (valor es

def soma_numeros(n1,n2):
    if n1 <= n2:
        soma = 0
        for i in range(n1, n2+1):
            if i % 2 == 1:
                soma += i
                
        return soma
                
    else:
        return None
    
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(soma_numeros(n1,n2))


