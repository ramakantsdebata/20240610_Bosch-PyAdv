from header import *

# . - represents any character except newline; If re.S specified, the newline is included as well

res = re.search(r'.+', string)
print(res)