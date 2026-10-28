import random

print("WELCOME To Number Guessing Game")
print("Choose Difficulty Level")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice = int(input("Enter level number (1/2/3): "))

if choice == 1:
    upper_limit = 50
elif choice == 2:
    upper_limit = 100
else:
    upper_limit = 500

computerNum = random.randint(1, upper_limit)

userNum = None


while userNum != computerNum:
    userNum = int(input("Enter Your Number: "))

    if abs(userNum - computerNum) <= 5 and userNum != computerNum:
        print("You are very close!")
    elif(computerNum < userNum):
        print("Too High! Try Again")
    elif(computerNum > userNum):
        print("Too Low! Try Again")
    elif(computerNum == userNum):
        print("CORRECT , You Guess The Number.")
        print("Computer Chose: ",computerNum)

print("THANK YOU AND PLAY AGAIN")