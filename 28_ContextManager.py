def BasicfileIO():
    file = open('testFile.txt', mode='w')
    try:
        file.write("This is sone text.\nSecondline")
    finally:
        file.close()

def WithContextManager():
    with open('testFile.txt', mode='w') as file:
        file.write("This is sone text.\nSecondline")



if __name__ == '__main__':
    BasicfileIO()
    BasicfileIO()