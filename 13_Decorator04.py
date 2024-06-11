class AddMethodDecorator:
    def __init__(self, method) -> None:
        self.method = method
        self.count = 0

    def __call__(self, *args, **kwArgs):
        self.count += 1
        print(f"[{self.count}] Calling {self.method.__name__} with args {args}, {kwArgs}")
        result = self.method(*args, **kwArgs)
        print(f"[{self.count}] Exiting {self.method.__name__}")
        return result



# obj = AddMethodDecorator(add)
# add(1, 2)  -->  obj(1, 2)


@AddMethodDecorator
def add(a, b):
    return a + b

@AddMethodDecorator
def sub(a, b):
    return a-b

print(add(1, 2))
print(add(5, 7))

print(sub(2, 1))
print(sub(6, 2))
print(sub(7, 1))
