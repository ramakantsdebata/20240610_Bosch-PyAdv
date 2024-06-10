# LEGB (Local, External, Global, Builtin)
'''
s1 = "Global"

def Function():
    # global s1
    # globals() - a dict of global objects
    # locals()  - a dict of local objects

    gbl = globals()
    lcl = locals()

    print("\n\n", "#"*80, sep='')
    print("\n", type(gbl), len(gbl), gbl)
    print("\n", type(lcl), len(lcl), lcl)
    print("\n", type(locals()), len(locals()), locals())
    print("\n\n", "#"*80, sep='')

    globals()['s1'] = "MODIFIED"

    s1 = "Function"

    def Inner():
        # nonlocal s1
        s1 = "Inner"
        print("Inner->", s1)

    # Inner() 
    print("Function->", s1)


Function()
print("Global->", s1)
'''


'''
def Outer(num):
    x = num
    def Inner(num2):
        print(x + num2)

    print("Outer")
    return Inner

ret = Outer(1)
ret2 = Outer(100)


ret(10)
ret2(50)

print(type(Outer))
'''
'''
def Foo(num):
    print(num)
    print(a)
    Bar()

def Bar():
    print("Bar")
    Baz()

def Baz():
    print("Baz")

a = 10
Foo(a)
'''

## Callback #############

## Publisher

sbsrs = []

def Register(fn):
    sbsrs.append(fn)

def RemoveSbsr(fn):
    sbsrs.remove(fn)

def NotifyAll(event):
    for fn in sbsrs:
        fn(event)

#################################

## Subscriber
def Do_something_about_it(event):
    print(f"Im handling it...{event}")

Register(Do_something_about_it)



print("Some time later ...")

# -------------------------------

## Event System
event = "rain'"
NotifyAll(event)

