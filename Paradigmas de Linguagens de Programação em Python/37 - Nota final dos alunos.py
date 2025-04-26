def soma(AV, AVA):
    final = [0]*n
    for i in range(n):
        final[i] = AV[i]+AVA[i]
    return final

def compara(AVA1, AVA2):
    AVA = [0]*n
    for i in range(n):
        if AVA1[i] >= AVA2[i]:
            AVA[i] = AVA1[i]
        else:
            AVA[i] = AVA2[i]
    return AVA

def cria_lista(n):
    nome = [0]*n
    AV = [0]*n
    AVA1 = [0]*n
    AVA2 = [0]*n
    for i in range(n):
        nome[i] = input(f"Digite o nome do {i+1}º aluno: ")
        AV[i] = float(input(f"Digite a nota da AV do {i+1}º aluno: "))
        AVA1[i] = float(input(f"Digite a nota do primeiro avaliando do {i+1}º aluno: "))
        AVA2[i] = float(input(f"Digite a nota do segundo avaliando do {i+1}º aluno: "))
    AVA = []
    AVA = compara(AVA1,AVA2)
    nota_final = []
    nota_final = soma(AV, AVA)
    print(nota_final)


n = int(input("Quantos alunos tem na turma? "))
cria_lista(n)
