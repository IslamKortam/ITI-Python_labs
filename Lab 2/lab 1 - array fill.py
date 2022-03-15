from readingModule import *
def fillArray(l):
    if not isinstance(l, list):
        return None
    length = readInt("Enter Length: ")
    start = readInt("Enter Start vale: ")
    for i in range(length):
        l.append(i + start)

l = []
fillArray(l)
print(l)
