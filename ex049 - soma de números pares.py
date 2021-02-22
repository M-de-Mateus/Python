pares = []
for c in range(0, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        pares.append(n)
print(sum(pares))
