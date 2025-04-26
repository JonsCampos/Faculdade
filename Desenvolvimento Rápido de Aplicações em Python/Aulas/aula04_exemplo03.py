'''
Aula04_exemplo03.py
'''
teste = 'Esta é uma simples mensagem'
#len() usado para encontrar o tamanho de uma string contando espaços e caracteres especiais.
print (len(teste)) #27
#replace() substitui uma string por outra.
teste = teste.replace('simples', 'curta')
print(teste) # Esta é uma curta mensagem
#count() exibe o número de vezes que uma string aparece dentro de outra string
print(teste.count('s')) #2
#find() exibe a posição que uma string esta ocupando dentro de outra string
print(teste.find('uma')) #7
