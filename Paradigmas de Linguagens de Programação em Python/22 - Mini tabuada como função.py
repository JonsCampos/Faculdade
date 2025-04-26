def calculo(a,b):
    print('----Mini Tabuada----')
    print('soma:', a + b)
    print('subtração:', a - b)
    print('multiplicação:', a * b)
    print('divisão:', a / b)
    print('Potenciação:', a**b)
    print('Resto da Divisão:', a%b)
    print('Divisão Arredondada:', a//b)


a = int(input('digite primeiro número: '))
b = int(input('digite segundo número: '))
calculo(a,b)
