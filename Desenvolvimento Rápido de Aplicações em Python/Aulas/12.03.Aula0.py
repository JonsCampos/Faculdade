with open('teste.txt', 'w', encoding='UTF-8') as arquivo:
    for i in range(100):
        arquivo.write(f'{i+1};\n')
