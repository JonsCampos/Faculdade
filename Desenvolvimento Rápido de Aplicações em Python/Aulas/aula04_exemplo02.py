#exemplo02.py
st = 'estou' 
s = ' em casa' 
print(st + s)  # estou em casa 
s = 'estou' ' em casa' 
print(s) 

#Interpolação:
st='vida boa' 
print("o comprimento de %s é %d" % (st,len(st)) )
#o comprimento de vida boa é 8 
#Uso da string como sequencia:
for c in s: 
    print(c) 

#particionando
st = 'Departamento de Sistemas e Computacao' 
print(st[:15]) #Departamento de 
print(st[27:]) #Computacao 
print(st[:15],st[27:]) #Departamento de Computacao
print(st[15:27])  # Sistemas e
print(st[::-1]) #oacatupmoC e sametsiS ed otnematrapeD 
