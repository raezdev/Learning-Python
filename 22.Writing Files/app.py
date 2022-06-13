file = open('e:/Proyectos/Learning Python/22.Writing Files/nuevo_paises.txt', 'w')
print(file.writable())
file.write('Este es el nuevo fichero de paises\n')
file.close()


file = open('e:/Proyectos/Learning Python/22.Writing Files/nuevo_paises.txt', 'a')
print(file.writable)
file.write('Este es una nueva linea\n')
file.close()