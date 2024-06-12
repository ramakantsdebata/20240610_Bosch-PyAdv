from header import *

# (?P<name>{expr})

res = re.search(r".+\s(?P<wordex>.*ex).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+).", string)
print(res.groups())
print(res.group(1), res.group(2), res.group(3), sep='---')
print(res.group('wordex'), res.group('uppercase'), res.group('date'), sep='---')
print(res.groupdict())
print(res.groupdict()['wordex'])

res = re.findall(r'\b(?P<word>\w+)\b\s(?P=word)', "It is a fine fine time in the the city.")
print(res)