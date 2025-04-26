class terreno:
    def __init__(self, x, y):
        self.a = x
        self.b = y
        print(x, y)

    def __str__(self):
        return 'Comprimento: %f, Largura: %f' % (self.a, self.b)

    def terrenoarea(self):
        return self.a * self.b


x = float(input('Digite o comprimento: '))
y = float(input('Digite a largura: '))
r = terreno(x, y)
print(r)
print('Área do terreno', r.terrenoarea())
