import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

res = re.search(r".+\s(.*ex).+(\d\d\s.+).", string)
print(res.span(1))
print(res.span(2))

print("Span -->", type(res.span()))
print(res.span(1)[0], res.span(1)[1])
# print(res.span(2))

print(res.start(1), res.end(1))
print(res.start(2), res.end(2))

