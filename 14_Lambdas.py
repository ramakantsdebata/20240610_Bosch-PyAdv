lst1 = [1, 2, 3, 4, 5, 6, 7]

# def square(num):
#     return num ** 2

tools = [lambda num: num ** 2, lambda num: num ** 3, lambda num: num ** 4]

lst2 = [tools[0](num)       for num in lst1]
print(lst2)

sqr1 = tools[0]
sqr2 = lambda num: num ** 2

print(sqr1(5))
print(sqr2(5))


'''
Sort(coll_Stud, lambda s1, s2: s1.Roll > s2.Roll)

def Sort(some_collection, comparator):
    if comparator(s1, s2):
        swap(s1, s2)'''