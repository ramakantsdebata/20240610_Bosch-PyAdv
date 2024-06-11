'''
from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a+b

@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3))
'''



class Car:

    __count = 0
    
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        # global count
        Car.__count += 1

    @classmethod
    def getCount(cls):
        return cls.__count

    def __str__(self):
        return f"This is a {self.model} by {self.make}."
    
    def __repr__(self):
        return f"self.make[{self.make}], self.model[{self.model}]."


print(f"'{Car.getCount()}' cars created.")

car1 = Car("Honda", "Accord")
car2 = Car("Toyota", "Camry")

print(car1) # --> print(str(car1)) --> print(car1.__str__()) --> print(car1.__repr__())
print(car2)

print(car1.__repr__())

# print(f"'{Car._Car__count}' cars created.")
print(f"'{car1.getCount()}' cars created.")

