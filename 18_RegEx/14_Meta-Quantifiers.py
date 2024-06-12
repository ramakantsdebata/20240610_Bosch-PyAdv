from header import *

def T1():
    # * - matches 0 or more, with as many repitions as possible
    #     Greedy match

    res =re.findall(r'\d\d\d*', string)
    print(res)

    res = re.findall(r'E\w*', string)
    print(res)


def T2():
    # + - matches 1 or more, with as many repitions as possible
    #     Greedy match

    res =re.findall(r'\d\d\d+', string)
    print(res)

    res = re.findall(r'E\w+', string)
    print(res)

def T3():
    # ? - matches 0 or 1
    #     Non-Greedy match

    res =re.findall(r'\d\d\d?', string)
    print(res)

    res = re.findall(r'E\w?', string)
    print(res)


def T4():
    res = re.findall(r'E\w*', string)
    print(res)

    res = re.findall(r'E\w*?', string)
    print(res)


    res = re.findall(r'E\w+', string)
    print(res)

    res = re.findall(r'E\w+?', string)
    print(res)


    res = re.findall(r'E\w?', string)
    print(res)

    res = re.findall(r'E\w??', string)
    print(res)


T4()