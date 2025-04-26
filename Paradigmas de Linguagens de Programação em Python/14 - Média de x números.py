quant = int(input('Qual a quantidade de números a ser digitados? '))
soma = 0
for i in range (1,quant+1):
    num = int(input(f'Digite o {i}º número: '))
    soma = soma + num
media = soma/quant
print('*'*30)
print(f'O valor da media dos valores corresponde à: {media}')
print('*'*30)
