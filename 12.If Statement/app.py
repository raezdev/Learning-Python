a = 4
b = 3
if (a > b) :
    print(str(a) + ' es mayor que ' + str(b))


a = 'Raez'
b = 'Raez'
if (a == b) :
    print('a es igual que b')


a = True
b = False
if a :
    print('a es True')
if b != True :
    print('b no es True')

a = 5
b = 6
if (a == b) :
    print('a es igual que b')
else:
    print('a no es igual que b')


a = 5
b = 6
if (a == b) :
    print('a es igual que b')
elif (a > b) :
    print('a es mayor que b')
else:
    print('a es menor que b')


a = False
b = False
if (a == True and b == True) :
    print('a y b son True')
elif (a == True or b == True ) :
    print('a o b son True')
else:
    print('ni a ni b son True')


valor = (input('Introduce un valor: '))
if (type(valor) == str):
    print('Valor es un String')
elif (type(valor) == int):
    print('Valor es un Integer')
elif (type(valor) == list):
    print('Valor es un List')
else:
    print('No se lo que es Valor')