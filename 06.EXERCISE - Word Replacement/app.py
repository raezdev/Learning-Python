from dataclasses import replace
from traceback import FrameSummary


frase = input('Introduzca una frase: ')
print('Su frase es: ' + frase)
palabra1 = input('Introduzca que palabra quiere reemplazar: ')
palabra2 = input('Introduzca por que palabra quiere reemplazar: ')
fraseFinal = frase.replace(palabra1, palabra2)
print('Su nueva frase es: ' + fraseFinal)
 
