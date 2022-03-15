word = input("Enter the word: ")
vowelsCount = 0
vowels = ('a', 'e', 'i', 'o', 'u')
for vowel in vowels:
    vowelsCount += word.count(vowel)
    vowelsCount += word.count(vowel.capitalize())
print(f"Number of vowels = {vowelsCount} vowel")