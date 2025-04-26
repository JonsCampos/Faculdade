def menu():
    print('*******************')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('*******************')

def soma(v1, v2):
    return v1+v2

def sub(v1, v2):
    return v1-v2

def mult(v1, v2):
    return v1*v2

def div(v1, v2):
    return v1/v2


v1 = int(input('Digite o valor do primeiro número: '))
v2 = int(input('Digite o valor do segundo número: '))
menu()
opcao = eval(input('Digite a opção desejada: '))
if opcao == 1:
    res = soma(v1, v2)
elif opcao == 2:
    res = sub(v1, v2)
elif opcao == 3:
    res = mult(v1, v2)
elif opcao == 4:
    res = div(v1, v2)
else:
    print('Opção Inválida')
    exit(0)
print(f'O resultado da operação é {res}')
