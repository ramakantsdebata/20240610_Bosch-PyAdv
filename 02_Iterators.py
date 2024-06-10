'''
st = set()

st.add(10)
st.add(20)
st.add("Test")

def add(a, b):
    return a+b
st.add(add)

lst = [1, 2, 3, 4]

print("\n Hashes -->")
print(hash(10))
print(hash(20))
print(hash("Test"))
print(hash(add))
# print(hash(lst))

# st.add(lst)

print(type(st), st)

tp = (1, 2, 3, 4, lst)
print(tp)
tp[4].append(5)
print(tp)
'''

lst = [1, 2, 3, 4, 5]
tp = (1, 2, 3, 4, 5)

for val in lst:
    print(val)

for val in tp:
    print(val)

ret = iter(lst) # lstr.__iter__()  --> returns an iterator; So 'ret' is an iterator
print(type(ret), ret)
while True:
    try:
        print("Val -->", next(ret)) # next(ret) --> ret.__next__()
    except StopIteration as ex:
        break
