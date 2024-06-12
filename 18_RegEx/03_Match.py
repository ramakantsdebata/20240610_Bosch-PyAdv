import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."


# Match - Similar to the search, but the match will be attempted from the beginning of the string

res = re.match(r"\d{4}", string)
print("Res -->", type(res), res)

res = re.match(r"\w{4}", string)
print("Res -->", type(res), res)

print(res.span())
print("Start-", res.start())
print("End-", res.end())

print(string[res.start(): res.end()])