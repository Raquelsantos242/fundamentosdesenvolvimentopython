res = []
res.append(input("Você come feijão preto frequentemente? (S/N) "))
#if res = "s"
#    res = res + 1
res.append(input("Você já passou pela ponte Rio x Niterói? (S/N) "))
res.append(input("metro = input('Você já pegou o metrô na estação carioca? (S/N) "))
res.append(input("Você já foi ao Rock In Rio? (S/N) "))

pontos=0
for r in res:
    if r == "s" or r == "S":
        pontos = pontos + 1
        
if pontos == 3 or pontos == 4:
    print("Certamente carioca")
elif pontos == 2 or pontos == 1:
    print("Possivelmente carioca")
else:
    print("não-carioca")
    
