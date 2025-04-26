mat = input('Digite o matrícula do aluno: ')
nome = input('Digite o nome do aluno: ')
av1 = float(input('Digite a nota da Av1 do aluno: '))
av2 = float(input('Digite a nota da Av2 do aluno: '))
media = (av1+av2)/2
if (media >= 6):
    print(f'{nome}, com matricula {mat} está aprovado com media {media}')
elif (media >=4):
    print(f'{nome}, com matricula {mat} está exame final')
else:
    print(f'{nome}, com matricula {mat} está reprovado')
