import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

res = re.search(r".+\s.*ex.+\d\d\s.+.", string)
print(res)
print(res.groups())

res = re.search(r".+\s(.*ex).+(\d\d\s.+).", string)
print(type(res), res)
print(res.groups())
print(res.group(1))
print(res.group(2))
print(res.group(0))
print(res.group())

print(res.group(1, 2))
