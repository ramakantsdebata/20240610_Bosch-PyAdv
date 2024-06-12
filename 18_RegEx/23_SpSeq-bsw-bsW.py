from header import *

res = re.findall(r'\w{5}', string)
print(res)

res = re.findall(r'\w{5}\W', string)
print(res)