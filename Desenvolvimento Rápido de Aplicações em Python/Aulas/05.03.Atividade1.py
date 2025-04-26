def numerosCrescente():
    arquivo = open('crescente.txt','w')

    for i in range(100):
        arquivo.write(str(i+1)+'; ')

    arquivo.close()

numerosCrescente()