class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = %s' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data


obj = FirstClass()
obj.setdata('hello')
obj.display()

obj2 = SecondClass()
# obj2.setdata(42)
obj2.display()

obj3 = ThirdClass('To the')
obj2.display()
obj3.__add__(' World')
obj3.display()
