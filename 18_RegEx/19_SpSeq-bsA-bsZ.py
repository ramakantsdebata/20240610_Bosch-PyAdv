import re

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

string2 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including 
the FTSE, fell by 11.48% – the worst day since it launched in 1998. 
The panic selling prompted by the coronavirus has wiped £2.7tn off the 
value of STOXX 600 shares since its all-time peak on 19 February.'''


# \A - Matches at the beginning of the string, as opposed to line.

res1 = re.findall(r"([A-Z].*)\s", string1)
res2 = re.findall(r"([A-Z].*)\s", string2)
print(res1, res2)

print("\n\n" + "#"*80)
res1 = re.findall(r"([A-Z].*?)\s", string1)
res2 = re.findall(r"([A-Z].*?)\s", string2)
print(res1, res2)

print("\n\n" + "#"*80)
res1 = re.findall(r"^([A-Z].*?)\s", string1, re.M)
res2 = re.findall(r"^([A-Z].*?)\s", string2, re.M)
print(res1, res2)

print("\n\n" + "#"*80)
res1 = re.findall(r"\A([A-Z].*?)\s", string1, re.M)
res2 = re.findall(r"\A([A-Z].*?)\s", string2, re.M)
print(res1, res2)

# \Z - End of entire string
print("\n\n" + "#"*80)
res1 = re.findall(r"\W$", string1, re.M)
res2 = re.findall(r"\W$", string2, re.M)
print(res1, res2)

print("\n\n" + "#"*80)
res1 = re.findall(r"\W\Z", string1, re.M)
res2 = re.findall(r"\W\Z", string2, re.M)
print(res1, res2)


# Summary:
# '^' and '$' operate on lines. Prominent when string input is multiline.
# '\A' and '\Z' operate on the whole string input, agnostic to it being a multiline or not.