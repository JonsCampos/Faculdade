def calculo(peso, altura):
    res = peso/(altura*altura)
    return res
def verificar(imc):
    situacao =''
    if (imc >= 40):
        situacao= 'Obesidade III'
    elif (imc >= 35):
        situacao= 'Obesidade II'
    elif (imc >= 30):
        situacao= 'Obesidade I'
    elif (imc >= 25):
        situacao= 'Acima do Peso'
    elif (imc >= 18.6):
        situacao= 'Peso Ideal'
    else:
        situacao = "Abaixo do Peso"
    return situacao


nome = input('Digite o nome do individuo: ')
peso = float(input('Digite o peso do individuo: '))
altura = float(input('Digite a altura do individuo: '))
imc = calculo(peso, altura) 
print(f'{nome} com peso = {peso:.2f} e altura = {altura:.2f}, Possui IMC={imc:.2f}')
sit = verificar(imc) 
print(f'{nome} esta com a situação: {sit}')
