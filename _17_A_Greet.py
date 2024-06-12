# __all__ = ['greet', 'greetName', 'greetInteractive']

def greet():
    print("Hello")

def greetName(name):
    print(helper("Hello", name))

def greetInteractive():
    name = input("Enter your name: ")
    print(helper("Hello", name))

def helper(greet, name):
    return greet + " " + name + "!"

if __name__ == "__main__":
    # def Tests():
    print("Testing...")
    greet()
    greetName("Vicky")
    # greetInteractive()
    helper("Test", "String")

# Tests()

# print(__name__)

# if __name__ == "__main__":
#     Tests()