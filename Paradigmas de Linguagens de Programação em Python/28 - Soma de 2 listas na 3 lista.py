x = int(input('Quantos elementos tem as lista? '))
list1 = [0]*x
list2 = [0]*x
list3 = [0]*x
print('Lendo a primeira lista de inteiros')
print('*'*30)
for i in range(x):
    list1[i] = int(input(f'Digite o {i+1}º elementos da lista 1: '))
print('Lendo a segunda lista de inteiros')
print('*'*30)
for i in range(x):
    list2[i] = int(input(f'Digite o {i+1}º elementos da lista 2: '))
print('Calculando a soma dos elementos')
print('*'*30)
for i in range(x):
    list3[i] = list1[i] + list2[i]
print(f'{list3}')
