class Car:

    __count = 0
    
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        Car.__count += 1

    @classmethod
    def getCount(cls):
        return cls.__count

    def __str__(self):
        return f"This is a {self.model} by {self.make}."
    
    def __repr__(self):
        return f"self.make[{self.make}], self.model[{self.model}]."
    
    def __lt__(self, other):
        if isinstance(other, Car):
            return self.year < other.year
        else:
            raise TypeError



car1 = Car("Honda", "Accord", 2015)
car2 = Car("Toyota", "Camry", 2005)
print(f"'{Car.getCount()}' cars created.")

if car1 < car2:
    print("Dated")
elif car1 > car2:
    print("Younger")
else: 
    print("Same year")

