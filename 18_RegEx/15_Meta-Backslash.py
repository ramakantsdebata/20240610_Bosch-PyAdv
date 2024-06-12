from header import *

# \ - Can have one of two meanings:
#       1. Special Sequences - \A, \b, \B, \d, \D, \w, \W, \s, \S, etc.
#       2. Escape character - \. \? \[ \] \^ \$

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

res = re.search(r".+\s(.*ex).+(\d\d\s.+).", string)
print(res.groups())

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February?"

res = re.search(r".+\s(.*ex).+(\d\d\s.+).", string)
print(res.groups())

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February!"

res = re.search(r".+\s(.*ex).+(\d\d\s.+).", string)
print(res.groups())

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

res = re.search(r".+\s(.*ex).+(\d\d\s.+)\.", string)
print(res.groups())


string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

res = re.search(r".+\s(.*ex).+(\d\d\s.+)", string)
print(res.groups())

res = re.findall(r".", string)
print(len(res))

res = re.findall(r"\.", string)
print(len(res))