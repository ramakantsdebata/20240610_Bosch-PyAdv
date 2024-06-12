from header import *

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

# A B C paterns are available
# if any of the patterns are matched, it should be successfully collected in to results
# A | B | C

res = re.search(r"\d{3}|\d{4}|\s[A-Z]{4}\s", string)
# \d{3}     |     \d{4}     |      \s[A-Z]{4}\s
print(res)

res = re.search(r"\d{8}|\d{4}|\W[A-Z]{4}\W", string)
print(res)