from math import degrees


def calcSum():
    sum = 0
    cnt = 0
    while True:
        x = input("Enter a number or done ")
        if x == "done":
            break
        if x.isnumeric():
            x = int(x)
            sum += x
            cnt += 1
        else:
            print("Error! not a number nor done")
    avg = sum/cnt
    return sum, avg


sum, avg = calcSum()
print(f"Sum = {sum}, avg = {avg}")