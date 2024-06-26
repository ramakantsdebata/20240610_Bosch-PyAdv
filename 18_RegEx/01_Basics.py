import re

path = r"\User\temp\newfile"
print(path)

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."


s = r"\d{4}"
print("S-->", type(s), s)

t = re.compile(s)
print("T-->", type(t), t)


res = t.findall(string)
print("Res ->", type(res), res)

res = re.findall(s, string)
print("Res ->", type(res), res)

res = re.findall(r"\w{3}", string)
print("Res ->", type(res), res)