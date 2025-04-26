quant = int(input('Qual a quantidade de números a ser digitados: '))
soma = 0
for i in range(quant):
    num = int(input(f'Digite o {i+1}º número: '))
    soma= soma + num
print(f'O valor do somatório é {soma}')