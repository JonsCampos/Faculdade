def menu():
    print('*******************')
    print('19 - João das Couves')
    print('33 - Amarildo')
    print('46 - Geremária')

def cria_lista(n):
    lista = [0]*n
    for i in range(n):
        lista[i]=int(input(f'Digite a intenção do voto do {i+1}º entrevistado: '))
    return lista

def voto(lis):
    canjc = cana = cang = BN = 0
    for i in range(n):
        if (lis[i] == 19):
            canjc += 1
        elif (lis[i] == 33):
            cana += 1
        elif (lis[i] == 46):
            cang += 1
        else:
            BN = BN+1
    print("\nTotal de Votos:")
    print("\nJoão \tAmarildo \tGeremária \tBranco-Nulos")
    print(f"{canjc/n*100:.2f}% \t{cana/n*100:.2f}% \t\t{cang/n*100:.2f}% \t\t{BN/n*100:.2f}%")


print("Conheça nosso candidatos")
menu()
lis = []
n = int(input("Quantos pessoas serão entevistas? "))
lis = cria_lista(n)
voto(lis)
