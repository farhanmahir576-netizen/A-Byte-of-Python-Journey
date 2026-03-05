class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Mahir')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Mahir').say_hi()
