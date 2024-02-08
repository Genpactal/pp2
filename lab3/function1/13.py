import random

rndm = random.randint(1, 20)

print("Hello! What is your name?")

name = input()

print("Well, " + name + " , I am thinking about number between 1 and 20")
print("Take a guess.")

ans = int(input())

cnt = 1

def guess_the_number(ans):

    if ans < rndm:
        print("Your guess is too low")
        print("Take a guess")
        return False
    elif ans > rndm:
        print("Your guess is too high")
        print("Take a guess")
        return False
    else: 
        print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses!")
        return True 
    
while(guess_the_number(ans) != True):
    ans = int(input())
    cnt += 1