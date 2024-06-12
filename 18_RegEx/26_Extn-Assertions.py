from header import *

'''
Positive Lookahead -    "({trg-pattern})(?={chk-pattern})"
Negative Lookahead -    "({trg-pattern})(?!{chk-pattern})"
Positive Lookbehind -   "(?<={chk-pattern})({trg-pattern})"
Negative Lookbehind -   "(?<!{chk-pattern})({trg-pattern})"
'''

res = re. findall(r'([A-Z]{5})\s(?=[0-9]{3})', string)
print(res)

res = re.findall(r"\b(\w+)\b(?!\s)", string)
print(res)

res = re.findall(r"(?<=,\s)\b(\w+)\b", string)
print(res)

res = re.findall(r"(?<!\s)\d{1,}", string)
print(res)