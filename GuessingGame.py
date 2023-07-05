import random

def run():
    GuessCount = 0
    SecretNumber = random.randint(0,9)
    level = input("> Enter Hard or Medium or Easy : ")
    print(" ")
    if level == "hard":
        GuessCount = 1
        print("you have Only 1 attempt to Guess ")
    elif level == "medium":
        GuessCount = 3
        print("You have 3 Chances")
    elif level == "easy":
        GuessCount = 5
        print("You have 5 Chances")
    else:
        print("Invalid")
        print(" ")
    AttemptCount = 0
    while GuessCount >  AttemptCount:
        GuessNumber = int(input("Whats Your Guess !!? "))
        if GuessNumber == SecretNumber:
            print(SecretNumber,"- Yahh itss Correct, Come Again")
            break
        else:
            AttemptCount+=1
            print("try again !")
    else:
        print("The answer is ",SecretNumber)

start = True
while start:
    message = input("> ").lower()
    if message == "start" or message == "1":
        run()
    elif message == "stop" or message == "2":
        break
    else:
        print("""
Welcome to the Guessing Game    
you have to Guess the number between 0-9 
your chance of attempts will be based on the difficulty level you choose
Type:
    start
    stop
    """)
else:
    print("Thank You :) , Come Again ")
