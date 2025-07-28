import random

print("This is a simple word-guessing game where the user has to guess the characters in a randomly selected word within a limited number of attempts. The program provides feedback after each guess, helping the user to either complete the word or lose the game based on their guesses.")
print("\n")
words = ['rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'geeks']
word =  random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed+=1
    
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    print()
    guess = input("Guess a character: ")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have ",+ turns," more guesses")

        if(turns == 0):
            print("You Lose")
            print("The word was: ", word)
            break

