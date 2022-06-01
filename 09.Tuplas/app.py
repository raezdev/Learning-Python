# Son inmutables
tres_numeros = (1, 2, 3)
print(tres_numeros)
print(tres_numeros[0])
print(tres_numeros[1])
print(tres_numeros[2])

# Error, es inmutable
#tres_numeros[1] = 23
#print(tres_numeros)

print(len(tres_numeros))
print(type(tres_numeros))

cadenas = ('hogar', 'tierra', 'mundo')
boo = (True, False, True)
mix = (1, 2, 3, 'hogar', False, 'tierra')
print(cadenas)
print(boo)
print(mix)
print(type(mix[0]))
print(type(mix[3]))
print(type(mix[4]))
