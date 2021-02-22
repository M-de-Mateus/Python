impares = []
for c in range(0, 500, 3):
    if c % 2 != 0:
        impares.append(c)
print(sum(impares))

