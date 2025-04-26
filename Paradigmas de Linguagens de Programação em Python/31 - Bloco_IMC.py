def calculo(peso, altura):
    res = peso/(altura*altura)
    return res


nome = input('Digite o nome do individuo: ')
peso = float(input('Digite o peso do individuo: '))
altura = float(input('Digite a altura do individuo: '))
imc = calculo(peso, altura)
print(f'{nome} com peso = {peso:.2f} e altura = {altura:.2f}, Possui IMC={imc:.2f}')
