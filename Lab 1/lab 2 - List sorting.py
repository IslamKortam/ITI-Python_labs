listSize = 5
list = []
for i in range(5):
    x = "a"
    while (not x.isnumeric() ) :
        x = input(f"Enter integer value at index {i}: ")
    x = int(x)
    list.append(x)
list.sort()
print("List sorted in assecding order: ", list)
list.sort(reverse=True)
print("List sorted in descending order: ", list)
