from header import *

res = re.findall(r'\bEuro\b', string) 
print(res)

res = re.findall(r'\b\w{4}\b', string) 
print(res)

res = re.findall(r'\Bcross', string) 
print(res)

