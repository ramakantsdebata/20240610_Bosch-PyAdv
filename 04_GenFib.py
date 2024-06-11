def FibGen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

it = FibGen(10)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

print("#"* 80)

for x in FibGen(10):
    print(x)