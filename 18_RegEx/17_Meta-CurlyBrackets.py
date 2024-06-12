from header import *

# {} - Quantifier; Can provide with min-max count

res = re.findall(r"\w{5}", string)
print(res)


res = re.findall(r"\s(\w{3,5})\s", string)
print(res)

res = re.findall(r"\s(\w{3,})\s", string)
print(res)

res = re.findall(r"\s(\w{,3})\s", string)
print(res)


number = "123432534645345747697696454"
res = re.search(r"\d{3,6}", number)
print(res)

number = "123432534645345747697696454"
res = re.search(r"\d{3,6}?", number)
print(res)

