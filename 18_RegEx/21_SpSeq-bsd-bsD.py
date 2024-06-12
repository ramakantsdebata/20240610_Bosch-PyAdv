# \d -  any digit
# \D - anything other than a digit

from header import *

res = re.findall(r"\d[a-z]", string)
print(res)

res = re.findall(r"\D[a-z]", string)
print(res)

res = re.findall(r'\W(\D)\W', string)
print(res)