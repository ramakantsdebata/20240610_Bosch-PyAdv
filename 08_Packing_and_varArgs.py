'''
lst = [1, 2, 3, 4, 5, 6]
others = []
a, b, c, *others  = lst

print(a, b, c, others, sep='\n')
'''

def add(a, b, *others, **kwMore):
    sum = a + b

    for x in others:
        sum += x

    for x in kwMore.values():
        sum += x

    return sum

# print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, 6))

print(add(1, 2, 3, ot2 = 4))
