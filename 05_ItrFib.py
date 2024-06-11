class FibGen:
    def __init__(self, num) -> None:
        self.num = num

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self

    def __next__(self):
        if self.count < self.num:
            x =self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return x
        else: 
            raise StopIteration

for x in FibGen(10):
    print(x, end= ' ')

print("All done")