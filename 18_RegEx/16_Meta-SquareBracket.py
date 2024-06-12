from header import *

# [] - class or set of sepcific characters
#    Can apply quantifiers to it

# Class [a-z] [A-Z] [0-9] [a-zA-Z]
# Set of chars - [aeiou]


res = re.findall(r'[aeiou]', string)
print(len(res), res)
res.sort()
print(len(res), res)


st = set(res)
if len(st) == 5:
    print("All vowels used")
else:
    print("something is missing")


res = re.findall(r'[xwrkt]', string)
print(len(res), res)

# \d - [0-9]
# \w - [0-9a-zA-Z_]
# \s - [ \n\t\v\f\r]
# Anything, but number - [^0-9]
# Anything, but a lower case character - [^a-z]