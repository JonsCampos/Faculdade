valor = int(input('Entre com um número para saber a tabuada: '))
print('*' * 18)
print(f'Tabuada de {valor}')
print('*' * 18)
for i in range(11):
    print(f'{valor} x {i} = {i*valor}')
