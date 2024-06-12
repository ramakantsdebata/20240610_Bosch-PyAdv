import re

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

string2 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including 
the FTSE, fell by 11.48% – the worst day since it launched in 1998. 
The panic selling prompted by the coronavirus has wiped £2.7tn off the 
value of STOXX 600 shares since its all-time peak on 19 February.'''

# $ - End of each line (if re.M is specified)

res = re.findall(r"\s(\w{2,})\W$", string1)
print(res)

res = re.findall(r"\s(\w{2,})\W$", string2)
print(res)

res = re.findall(r"\s(\w{2,})\W$", string2, re.M)
print(res)