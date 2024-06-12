import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

# re.search(pattern, sub_str)
# returns a match object

res = re.search(r"\d{3}", string)
print("Res -->", type(res), res)
# Res --> <class 're.Match'> <re.Match object; span=(15, 18), match='600'>
# Span --> Slice of the subject string
print(string[15:18])