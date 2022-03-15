import random
import os
from time import sleep
from turtle import clearscreen
from unicodedata import name
from readingModule import *

words = ["cat", "chair", "book", "human", "code"]

userName = "123"
while not userName.isalpha() :
    userName = readNonEmptyString("Enter name(Non empty string of alphapets: ")

randomWord = words[random.randint(0, len(words) - 1)]
originalRandomWord = randomWord
guessedWord = len(randomWord) * '*'
print(f"Hello, {userName}")

for i in range(1, 8) :
    
    print(f"Ateempt #{i}: ")
    print(f"You guessed: {guessedWord}")
    c = readOneAlphapet("Enter an Alphabet: ")
    c = c.lower()
    index = randomWord.find(c)
    if ~index:
        guessedWordList = list(guessedWord)
        randomWordList = list(randomWord)
        guessedWordList[index] = randomWord[index]
        randomWordList[index] = '*'
        guessedWord = "".join(guessedWordList)
        randomWord = "".join(randomWordList)
        print("success! your guess is perfect!")
        print(f"till now you guessed: '{guessedWord}'")
        lettersLeft = guessedWord.count('*')
        if lettersLeft == 0:
            print(f"Congratulations, {userName}\nYou win!")
            loseFlag = False
            break
        else:
            print(f"You have {7 - i} attempts left, and {lettersLeft} chars to guess!\nGo On")
    else:
        print('Wrong guess, try again')

    sleep(1.5)
    os.system('cls')


