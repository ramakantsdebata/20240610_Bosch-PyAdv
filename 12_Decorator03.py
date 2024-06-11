
def add_tags(cls):
    class Wrapper(cls):
        def __init__(self, value = ""):
            super().__init__()
            # self.value = value
            if value == "":
                self._tags = list()
            else:
                self._tags = list([value,])

        @property
        def tags(self):
            print(f"[[Getting all tags]]", end=' ') #: {self._tags}")
            return self._tags
        
        @tags.setter
        def tags(self, value):
            print(f"Setting a new tag:{value}")
            self._tags.append(value)
    return Wrapper



@add_tags
class Number:
    def __init__(self) -> None:
        pass

num = Number()

# num.tags("Python")
num.tags = "Python"
num.tags = "Training"
num.tags = "Coimbatore"

print("Tags --> ", end='')
for x in num.tags:
    print(x, end=' ')
print()


'''
lst = [1, 2, 3, 4, 5]
lst2 = list(lst)
lst2.append(10)
lst2.append(lst)

# lst3 = list(20)

# [[1, 2, 3, 4, 5], 10]

# [1, 2, 3, 4, 5, 10]
print(lst2)
'''