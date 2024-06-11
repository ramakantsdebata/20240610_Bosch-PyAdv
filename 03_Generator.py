'''
lst = [1, 2, 3, 4, 5]

for x in range(len(lst)):
    print(lst[x])
'''

def SimpleGen():
    print("First yield", end=' ')
    yield 1
    print("Second yield", end=' ')
    yield 2
    print("Third yield", end=' ')
    yield 3
    print("Fourth yield", end=' ')
    yield 4


## Using a regular function
# print(SimpleGen())
# print(SimpleGen())
# print(SimpleGen())

## Using a generator
itr = SimpleGen()
'''
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
'''

while True:
    try:
        print(next(itr))
    except StopIteration:
        print("All done")
        break

print("Finished printing")


'''
f= open(fileName, 'w')

try:
    f.write(data)
    # f.close()
except FileNotFoundError as ex:
    print("Exception->", ex)
    # Handle the exception
finally:
    f.close()

## Context Managers

with open(fileName, 'w') as f:
    f.write(data)

print("All done")
'''