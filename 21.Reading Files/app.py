file = open('e:/Proyectos/Learning Python/21.Reading Files/paises.txt', 'r')
print(file.readable())
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()


file = open('e:/Proyectos/Learning Python/21.Reading Files/paises.txt', 'r')
print(file.readable())
print(file.readlines())
file.close()


file = open('e:/Proyectos/Learning Python/21.Reading Files/paises.txt', 'r')
print(file.readlines()[2])
file.close()

file = open('e:/Proyectos/Learning Python/21.Reading Files/paises.txt', 'r')
for line in file.readlines():
    print(line)
file.close()