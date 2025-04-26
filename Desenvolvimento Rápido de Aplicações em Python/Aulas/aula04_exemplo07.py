'''
Aula04_exemplo07.py

#sem tratamento
for linha in open('meuarquivo.txt','r'):
    print(linha, end="")
'''

#com tratamento e fechando o arquivo automaticamente após o uso
try:
    with open('meuarquivo.txt','r') as f:
        for linha in f:
            print(linha, end="") #sem pular linha
except FileNotFoundError:
    print('Arquivo não encontrado')

