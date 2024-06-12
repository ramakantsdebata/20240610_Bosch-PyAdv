from header import *

string2 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including 
the FTSE, fell by 11.48% – the worst day since it launched in 1998. 
The panic selling prompted by the coronavirus has wiped £2.7tn off the 
value of STOXX 600 shares since its all-time peak on 19 February.'''

res = re.findall(r'\s', string2)
print(res)

res = re.findall(r'\S{8}', string2)
print(res)
