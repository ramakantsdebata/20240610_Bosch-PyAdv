from header import * 

# Extn notation - (?{extn}{expr})
# Non-capturing - (?:{expr})
res = re.search(r".+\s(.*ex).+(\d\d\s.+).", string)
print(res.groups())
print(res.group(1))

res = re.search(r".+\s(?:.*ex).+(\d\d\s.+).", string)
print(res.groups())
print(res.group(1))
