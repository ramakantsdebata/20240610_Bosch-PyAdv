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
    def wrapper():
        print(f"'{fn.__name__}' called")
        fn()
        print(f"'{fn.__name__}' returned")
    return wrapper


# greet = addlogs(greet)

@addlogs
def greet():
    print("Hello")


@addlogs
def MentionOrg():
    print("Bosch")


## Consumer code #############
greet()
# wrapper()

MentionOrg()