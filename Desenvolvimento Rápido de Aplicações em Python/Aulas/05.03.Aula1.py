def gerarListaOrdenada():
    quant = int(input('Informe a quantidade de elementos: '))
    arquivo = open('idsOrdenados.txt','w')

    for elemento in range(quant):
        arquivo.write(str(elemento)+' ')

    arquivo.close()

def gerarListaOrdenadaWL():
    lista = []
    quant = int(input('Informe a quantidade de elementos: '))
    arquivo = open('idsOrdenadosWriteLines.txt','w')

    for elemento in range(quant):
        lista.append(str(elemento)+' ')

    arquivo.writelines(lista)
    arquivo.close()


gerarListaOrdenada()
gerarListaOrdenadaWL()