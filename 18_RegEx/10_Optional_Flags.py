import re

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

string2 = '''The Euro STOXX 600 index, which tracks all stock markets across Europe including 
the FTSE, fell by 11.48% – the worst day since it launched in 1998. 
The panic selling prompted by the coronavirus has wiped £2.7tn off the 
value of STOXX 600 shares since its all-time peak on 19 February.'''


# re.I - IGNORECASE
# re.M - MULTILINE
# re.S - DOTALL
# re.X - VERBOSE
# flags = re.I | re.M | re.S | re.X

## Ignorecase
res  = re.findall(r"the", string1, re.I)
print(res)

## Multiline
res  = re.findall(r"^The", string2, re.M)
print(res)

## DOTALL
res  = re.findall(r".+", string2, re.S)
print(len(res))

## Verbose
res = re.search(r'''.+\s    # Starting of the string
                (.*ex)      # A word ending with 'ex'
                .+          # Anything in between
                (\d\d\s.+)  # Date
                . #Exactly one character ''', string1, re.X)
print(res.groups())