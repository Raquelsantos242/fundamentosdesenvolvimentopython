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


