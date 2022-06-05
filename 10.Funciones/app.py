
def greetings_function():
    print('Welcome User')

greetings_function()


def welcome_function(name):
    print('Welcome ' + str(name))

welcome_function('Raez')
welcome_function(5)


def welcome3_function(*names):
    print('Welcome ' + names[1])

welcome3_function('Pedro', 'Pablo', 'Manuel')


def welcome2_function(name, age):
    print('Welcome ' + str(name) + ', you are ' + str(age))

welcome2_function('Raez', 37)
welcome2_function(name = 'Raez', age = 37)

name = input('Enter your name: ')
age = input('Enter your age: ')
welcome2_function(name, age)





