arquivo = open('idsOrdenados.txt','r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close

arquivo2 = open('idsOrdenadosWriteLines.txt','r')
linhas = arquivo2.readline()
for linha in linhas:
    print(linha)
arquivo2.close