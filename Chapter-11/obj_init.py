class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, {} how are you?'.format(self.name))

p = Person('Mahir')
p.say_hi()
