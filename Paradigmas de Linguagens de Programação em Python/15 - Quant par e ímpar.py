quant = int(input('Qual a quantidade de números a ser digitados? '))
par=0
impar=0
for i in range(1,quant+1):
    num=int(input(f'Digite o {i}º número: '))
    if(num%2==0):
        par+=1
    else:
        impar+=1
print(f'Dos {quant} números digitados temos {par} números pares')
print(f'Dos {quant} números digitados temos {impar} números ímpares')
