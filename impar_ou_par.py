def valor():
    v = int(input('Digite um valor'))


num = [[],[]]
v = 0
for c in range(1,6):
    v = int(input('Digite um valor: '))
    if v %2 == 0: # é par
        num[0].append(v)
    else:
        num[1].append(v)

print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
