'''
Aula04_exemplo05.py
'''
a = [ 1, 2, 3 ]
try:
	print(a[5])
except IndexError:
	print("Posição inexistente!")
finally:
	print("Fim do teste")
