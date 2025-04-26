# This is a sample Python script.
from tkinter import messagebox

from Aluno import Aluno


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def executar():
    # pass # palavra reservada só para completar o código
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    lista = []
    messagebox.showinfo("Teste","Bemvindo ao PyCharm")
    #criar o objeto Aluno
    aluno1 = Aluno(123,'Maria',8.5)
    #entrada de dados
    aluno1.matricula = 321
    aluno2 = Aluno(555,'José',7.2)
    #processamento
    lista.append(aluno1)
    lista.append(aluno2)

    #saída de dados
    saida = ""
    for aluno in lista:
        saida += aluno.obterdados() + '\n'
    messagebox.showinfo("Lista de alunos", saida)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
