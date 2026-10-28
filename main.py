import random

while True:
    user_input = input("Playing Game [YES/NO]:  ").lower()
    if user_input == "no":
        print("Thank You for Playing")
        break
    elif user_input == "yes":
        print("1. Level Easy [1-50]")
        print("2. Level Medium [1-200]")
        print("3. Level Hard [1-500]")

        choise = input("Enter Your Level: ").lower()
        
        if choise == "1" or "easy":
            easy_choise = random.randint(1,50)
            score = 0
            while True:
                easy_input = int(input("Enter Your Choise Number: "))
                score += 1
                if easy_choise == easy_input:
                    print("You are Correct✅")
                    print("Your Score: ",score)
                    break
                elif easy_choise > easy_input:
                    print("Low")
                elif easy_choise < easy_input :
                    print("High")


        elif choise == "2" or "medium":
            medium_choise = random.randint(1,200)
            score = 0
            while True:
                medium_input = int(input("Enter Your Choise Number: "))
                score += 1
                if medium_choise == medium_input:
                    print("You are Correct✅")
                    print("Your Score: ",score)
                    break
                elif medium_choise > medium_input:
                    print("Low")
                elif medium_choise < medium_input :
                    print("High")


        elif choise == "3" or "hard":
            hard_choise = random.randint(1,500)
            score = 0
            while True:
                hard_input = int(input("Enter Your Choise Number: "))
                score += 1
                if hard_choise == hard_input:
                    print("You are Correct✅")
                    print("Your Score: ",score)
                    break
                elif hard_choise > hard_input:
                    print("Low")
                elif hard_choise < hard_input :
                    print("High")

