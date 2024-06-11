'''
## Stage 1
def greet():
    print("Hello")

def wrapper():
    print("'greet()' called")
    greet()
    print("'greet()' returned")
'''

'''
## Stage 2
temp = greet

def greet():
    print("'greet()' called")
    temp()
    print("'greet()' returned")
'''


def addlogs(fn):
    def wrapper(*args, **kwArgs):
        print(f"'{fn.__name__}' called")
        result = fn(*args, **kwArgs)
        print(f"'{fn.__name__}' returned")
        return result
    return wrapper


# greet = addlogs(greet)

@addlogs
def greet():
    print("Hello")


@addlogs
def MentionOrg():
    print("Bosch")


@addlogs
def add(a, b):
    return a+b

## Consumer code #############
greet()
# wrapper()

MentionOrg()

print(add(1, 2))




