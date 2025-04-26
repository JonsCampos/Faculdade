'''
Aula04_exemplo04.py
'''
teste = '   Outra simples mensagem   '
#strip() remove os espaços no início e no final da string.
print(teste.strip()) #Outra simples mensagem
#split() divide uma string em uma lista onde cada palavra é um item de lista.
x = teste.split()
print(x) #exibe ['Outra', 'simples', 'mensagem']
#join() junta todos os itens de uma tupla em uma string, usando um caractere de hash como separador
minhaTupla = ("John", "Peter", "Vicky")
x = " ".join(minhaTupla)
print(x) # exibe : John#Peter#Vicky
teste2 = input("Digite um nome: ")
#strip() remove os espaços no início e no final da string.
print(teste2)
print(teste2.strip())
