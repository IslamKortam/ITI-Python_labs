word = input("Enter your word: ")
lowerCaseVowels = ('a', 'e', 'i', 'o', 'u')
upperCaseVowels = ('A', 'E', 'I', 'O', 'U')
vowels = lowerCaseVowels + upperCaseVowels

ans = ""
for i in range(len(word)) :
    if not (word[i] in vowels) :
        ans += word[i]
print(ans)