import random

print("Hello welcome to the number guessing game !")
low = int(input("Enter the lower bound: "))
high = int(input("Enter the higher bound: "))

print("\n You have 5 chances to guess the correct number. So lets begin !")

num = random.randint(low,high)
ch=5
gc=0
run=True

while run :
    gc+=1
    guess =int((input("\n Enter you guess: ")))
    
    if guess == num:
        print("You guessed it right man!")
        ans = input("Do you wanna try again ? (y/n)")
        if ans == 'y':
            run=True
            num = random.randint(low,high)
            gc=0
            continue
        else:
            run=False
            break
    elif guess < num:
        print("Your guess is too low! ")
    elif guess > num:
        print("Your guess is too high smartass ! think more retarded")
    elif gc >= ch and guess != num:
        print(f"The num was {num}")
        ans = input("Do you wanna try again ? (y/n)")
        ans = ans.lower
        if ans == 'y':
            run=True
            num = random.randint(low,high)
            gc=0
        else:
            run=False
        break