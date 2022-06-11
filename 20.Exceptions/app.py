try:
    x= int(input('Introduzca un numero entero: '))
    print(x)
except:
    print('Algo ha ido mal.')


try:
    x= int(input('Introduzca un numero entero: '))
    print(x)
except ValueError:
    print('ERROR - El valor introducido no es un entero.')


try:
    x= int(input('Introduzca un numero entero: '))
    print(x)
except ValueError:
    print('ERROR - El valor introducido no es un entero.')
else:
    print('Ejecucion correcta.')


try:
    x= int(input('Introduzca un numero entero: '))
    print(x)
except ValueError:
    print('ERROR - El valor introducido no es un entero.')
else:
    print('Ejecucion correcta.')
finally:
    print('Try-Excep Finalizado')