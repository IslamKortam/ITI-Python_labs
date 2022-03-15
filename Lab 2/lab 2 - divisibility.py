from readingModule import *

def bizzFuzz(n):
    if not isinstance(n, int):
        return None
    ret = ""
    if n % 3 == 0 :
        ret += "Fizz"
    if n % 5 == 0 :
        ret += "Buzz"
    return ret


x = readInt("Enter n: ")
print(bizzFuzz(x))