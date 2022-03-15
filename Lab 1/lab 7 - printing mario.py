height = "string"
while not height.isnumeric() : 
    height = input("Enter height (numeric value): ")
height = int(height)

for i in range(1, height + 1) : 
    row = ((height - i) * ' ') + (i * '*')
    print(row)


