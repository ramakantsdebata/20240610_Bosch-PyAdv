class Example:
    def __init__(self, val) -> None:
        self.val = val
        print("Initialising the object.")

    def __del__(self):
        print("Object being destroyed; Releasing resources.")

    def __delete__(self, instance):
        print(f"__delete__, {instance}")

# class Foo:
#     exmp = Example(7)


def Test1():
    exm = Example(5)

    print("\n\nDo some work\n\n")

    print("Exiting block")


def Test2():
    exm = Example(10)
    del exm
    print("Exiting AnotherMain()")

def Test3():
    a = Example(3)
    b = a
    print(id(a), id(b))
    print("Deleting 'a'")
    del a
    print("Deleting 'b'")
    del b

def Test4():
    f= Foo()
    del f.exmp
    print(f)


class Test:
    def __init__(self) -> None:
        self.x = 10
        self.y = 20

def Test5():
    test = Test()
    print(test.__dict__)
    test.__dict__[0] = 100
    del test.__dict__['x']
    print(test.__dict__)
    

def Main():
    # Test1()
    # Test2()
    # Test3()
    # Test4()
    Test5()
    print("Last line")

Main()