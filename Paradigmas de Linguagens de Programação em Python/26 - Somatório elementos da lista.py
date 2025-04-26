n = int(input('Digite quantos elementos possui o vetor: '))
lista = [0]*n
soma = 0
for i in range(n):
    lista[i] = int(input(f'Digite o {i+1}º valor: '))
    soma += lista[i]
print(lista)
print(f'O somatório dos elementos é igual: {soma}')
