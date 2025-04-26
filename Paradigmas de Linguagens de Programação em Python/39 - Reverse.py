vetor = [ ]
continua = "s"
while(continua == "s" or continua == "S"):
    vetor.append(int(input("Digite um valor para o vetor: ")))
    continua = input("Deseja continuar? Digite s para sim ou n para não: ")
vetor.reverse()
print(vetor)
