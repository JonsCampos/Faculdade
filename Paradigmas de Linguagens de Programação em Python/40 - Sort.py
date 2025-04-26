lista = [ ]
continua = "s"
while(continua == "s" or continua == "S"):
    lista.append(int(input("Digite um valor para a inserir na lista: ")))
    continua = input("Deseja continuar? Digite s para sim ou n para não: ")
lista.sort()
print(lista)