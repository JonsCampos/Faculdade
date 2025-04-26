'''
Aula04_exemplo06.py
'''
try:
    a = int(input('Digite um número:'))
    b = int(input('Digite um número para dividir com o primeiro:'))
    n = a/b
except ZeroDivisionError: #divisão por zero
    print('Não é possível dividir um número por zero')
except ValueError: #erro de valor
    print('Tivemos um problema com os dados fornecidos')
except KeyboardInterrupt: #interrompeu programa com CRTL C
    print('O usuário interrompeu a execução do programa')
else:
    print("A divisão foi " + str(n)) #foi tudo bem
finally:
    print('Obrigado, volte sempre!') #sempre é executado
