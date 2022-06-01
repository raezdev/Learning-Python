list1 = [1, 2, 3, 4, 5]
list2 = ['platano', 'manzana', 'mango', 'naranja']
print(list1)
print(list2)

list1.extend(list2)
print(list1)

list2.append('cecera')
print(list2)
print(len(list2))

list2.insert(1, 'sandia')
print(list2)
print(len(list2))

list2.remove('platano')
print(list2)
print(len(list2))

list2 = ['platano', 'manzana', 'mango', 'naranja', 'mango']
print(list2.index('manzana'))
print(list2.count('mango'))

list1 = [4, 3, 5, 1, 2]
list2 = ['platano', 'manzana', 'mango', 'naranja']
list1.sort()
list2.reverse()
print(list1)
print(list2)

list1 = [4, 3, 5, 1, 2]
list2 = ['platano', 'manzana', 'mango', 'naranja']
list3 = list2.copy()
list2.pop()
print(list3)
print(list2)
list2.pop(1)
print(list2)
del list3[2]
print(list3)
