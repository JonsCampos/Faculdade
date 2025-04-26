n = int(input('Digite quantos elementos possui o vetor: '))
lista = [0]*n
produto = 1
for i in range(n):
    lista[i] = int(input(f'Digite o {i+1}º valor: '))
    produto *= lista[i]
print(lista)
print(f'O produtório dos elementos é igual: {produto}')
