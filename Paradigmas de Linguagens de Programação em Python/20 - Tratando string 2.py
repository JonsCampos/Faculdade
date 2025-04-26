frase= input('Entre com uma frase: ')
cont = 0
for i in frase:
    if (i != ' '):
        cont = cont + 1
print(f'Na frase digitado temos {cont} caracteres')