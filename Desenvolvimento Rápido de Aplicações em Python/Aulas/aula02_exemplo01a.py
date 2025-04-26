'''Aula 02 - exemplo01a.py
função : Sistema de registro de notas de alunos - 
Instituição pequena (i)
Vantagens do RAD : Entregar o sistema através dos processos gerando
protótipos que serão gradativamente atualizados. O conjunto de dados
será menor do que o cenário (ii).
Desvantagens do RAD : Exige uma equipe de desenvolvimento bem qualificada
 o que neste cenário será viável pois o porte do sistema será pequeno em
relação ao cenário (ii).
Modelo de negócio : A instituição ministra aulas em turmas de alunos de
 algumas áreas : TI, Administração e Direito. Cada aluno deve ser
matriculado em uma turma de cada curso. As disciplinas serão ministradas
por poucos docentes em suas respectivas áreas.
'''
#funções modulares
#cadastrar os dados do aluno
def cadastrar_aluno(lista,matricula):
    nome  = input("Informe o nome do aluno:")
    curso = input("Escolha o curso: 1-TI 2-Administração 3-Direito: ")
    turma = input("Informe o código da turma:")
    aluno = [matricula,nome,curso,turma]
    lista.append(aluno)

def principal():
    print("Sistema de registro de notas - Instituição XYZ (i)")

    #entrada de dados
    print("Cadastro de aluno novo")
    #variável local
    lista = [] #lista vazia
    for i in range(2):
        matricula = "000"+str(i+1)
        print("Aluno: Matricula" + matricula)
        cadastrar_aluno(lista,matricula) #guardar os 3 alunos
    exibir_lista(lista)

#mostrar os alunos cadastrados
def exibir_lista(lista):
    for a in range(2):
        print(lista[a])

#principal
principal()
print("Fim do programa")