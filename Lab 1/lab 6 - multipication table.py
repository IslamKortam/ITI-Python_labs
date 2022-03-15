x = "string"
while not x.isnumeric() : 
    x = input("Enter numeric value: ")
x = int(x)
table = []
for i in range(1, x + 1) :
    row = []
    for j in range(1, i + 1) :
        row.append(j * i)
    table.append(row)
print(table)