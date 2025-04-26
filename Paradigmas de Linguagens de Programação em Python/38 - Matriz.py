lin = int(input("Digite o número de linhas da matriz: "))
col = int(input("Digite o número de colunas da matriz: "))
matriz = []
for i in range(lin):
    linha = []
    for j in range(col):
        valor = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)
print(matriz)
soma = 0
for i in range(lin):
    for j in range(col):
        soma = soma + matriz[i][j]
print(f"A soma é {soma}")
