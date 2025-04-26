cpf= input('Digite o matrícula do cidadão: ')
nome = input('Digite o nome do cidadão : ')
idade= int(input('Digite a idade do cidadão : '))
if (idade >= 18) and (idade<70):
    print(f'O cidadão inscrito no cpf número {cpf} é eleitor obrigatório')
elif (idade>=16) and (idade<18) or (idade>=70):
    print(f'O cidadão inscrito no cpf número {cpf} é eleitor facultativo')
else:
    print(f'O cidadão inscrito no cpf número {cpf} é não eleitor ')
