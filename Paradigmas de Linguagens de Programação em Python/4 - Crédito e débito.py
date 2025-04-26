conta = input('Digite o numero da conta do Cliente: ')
credito = float(input('Digite o valor do crédito do cliente: R$ '))
debito = float(input('Digite o valor do débito do cliente: R$ '))
saldo = credito - debito
if (saldo>=0):
    print(f'O cliente da conta número {conta} está com saldo positivo em R$ {saldo}')
else:
    print(f'O cliente da conta número {conta} está com saldo negativo em R$ {saldo}')
