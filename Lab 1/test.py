from tkinter.messagebox import RETRY


def fibbonacci(x):
    if x < 2 :
        return x
    print(x)
    return fibbonacci(x - 1) + fibbonacci(x - 2)


fib = fibbonacci(60)
print(f"resupt = {fib}")
