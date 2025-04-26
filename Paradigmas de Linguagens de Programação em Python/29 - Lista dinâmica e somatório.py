continua = 's'
lista = []
while (continua == 's' or continua == 'S'):
    n = eval(input('Digite um numero: '))
    lista.append(n)
    continua = input('Deseja continuar? s para sim e n para não')
print(lista)
soma = 0
for i in range(len(lista)):
    soma = soma + lista[i]
print(soma)
