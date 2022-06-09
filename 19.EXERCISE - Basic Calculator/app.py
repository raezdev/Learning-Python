def pintar_menu():
    print('***** MENU CALCULADORA *****')
    print('1 - Sumar')
    print('2 - Restar')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('S - Salir')
    opcion = input('Seleccione una opcion: ')
    return opcion

def sumar():
    print('Ha seleccionado sumar')
    sum1 = int(input('Introduzca el primer numero: '))
    sum2 = int(input('Introduzca el segundo numero: '))
    print(sum1, '+', sum2, '=', sum1+sum2)

def restar():
    print('Ha seleccionado restar')
    sum1 = int(input('Introduzca el primer numero: '))
    sum2 = int(input('Introduzca el segundo numero: '))
    print(sum1, '-', sum2, '=', sum1-sum2)

def multiplicar():
    print('Ha seleccionado multiplicar')
    sum1 = int(input('Introduzca el primer numero: '))
    sum2 = int(input('Introduzca el segundo numero: '))
    print(sum1, '*', sum2, '=', sum1*sum2)

def dividir():
    print('Ha seleccionado dividir')
    sum1 = int(input('Introduzca el primer numero: '))
    sum2 = int(input('Introduzca el segundo numero: '))
    print(sum1, '/', sum2, '=', sum1/sum2)

opt = pintar_menu()
while opt != 'S' and opt != 's':
    if opt == '1':
        sumar()
    elif opt == '2':
        restar()
    elif opt == '3':
        multiplicar()
    elif opt == '4':
        dividir()
    else:
        print('Opcion no valida')
    opt = pintar_menu()

