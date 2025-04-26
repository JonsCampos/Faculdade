cpf= input('Digite o matrícula do cidadão: ')
nome = input('Digite o nome do cidadão : ')
renda= float(input('Digite a renda do cidadão : '))
if(renda>=4664.68):
    print(f'Cidadão inscrito no CPF número {cpf} está na alíquota de 27,5% do imposto de renda')
elif(renda>=3751.06 ):
    print(f'Cidadão inscrito no CPF número {cpf} está na alíquota de 22,5% do imposto de renda')
elif(renda>=2826.66 ):
    print(f'Cidadão inscrito no CPF número {cpf} está na alíquota de 15% do imposto de renda')
elif(renda>=2112.01 ):
    print(f'Cidadão inscrito no CPF número {cpf} está na alíquota de 7,5% do imposto de renda')
else:
    print(f'Cidadão inscrito no CPF número {cpf} está na alíquota de 0% do imposto de renda')
