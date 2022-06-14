print('*** CREACION DE USUARIO ***')
createUser = input('Introduzca el usuario a crear: ')
createPass = input('Introduzca la password: ')
print('Usuario creado correctamente.')

print('\n')
print('\n')

print('*** LOGADO DE USUARIO ***')
username = input('Introduzca su login: ')
password = input('Introduzca su password: ')
if (username == createUser and password == createPass):
    print('Usuario logado correctamente.')
else:
    print('Credenciales invalidas.')




