def generateLongestSubstring(x):
    if not isinstance(x, str) : 
        return None
    
    length = len(x)
    if length < 2 :
        return x
    
    listOfChars = list(x)
    maxSubStringLength = 1
    maxSubString = listOfChars[0]
    orderdCharsCount = 1
    orderdString = listOfChars[0]
    for i in range(1, length):
        if listOfChars[i] > listOfChars[i - 1]:
            orderdString += listOfChars[i]
            orderdCharsCount += 1
            if orderdCharsCount >= maxSubStringLength:
                maxSubStringLength = orderdCharsCount
                maxSubString = orderdString
        else:
            orderdCharsCount = 1
            orderdString = listOfChars[i]
    
    return maxSubString


string = input("Enter a string: ")
maxSubString = generateLongestSubstring(string)
print(f"Max substring:{maxSubString}")