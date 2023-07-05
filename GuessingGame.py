import random

SecretNumber = random.randint(0,5)
GuessCount = 3
AttemptCount = 0
while GuessCount >  AttemptCount:
    GuessNumber = int(input("Whats Your Guess !!? "))
    if GuessNumber == SecretNumber:
        print(SecretNumber,"- Yahh itss Correct, Come Again")
        break
    else:
        AttemptCount+=1
else:
    print("The answer is ",SecretNumber)