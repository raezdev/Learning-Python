class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Persona('Raez', 37)
print(p2.name)
print(p2.age)