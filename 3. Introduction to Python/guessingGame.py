import random

ddef computerGuess(lowval, highval, randnum, count=0):
if highval >= lowval:
    guess = lowval + (highval - lowval) // 2
    if guess == randnum:
        return count

    elif guess > randnum:
        count = count + 1
        return computerGuess(lowval, guess-1, randnum, count)
else:
    return -1
#Get the user's guess
randnum = random.randint(1,101)

count = 0
guess = -99

while (guess !=randnum):
        guess =(int) (input("Enter your guess between 1 and 100:"))
        if guess < randnum:
                print("higher")
        elif guess > randnum:
                print("lower")
        else:
                print("you guessed it!")
                break
        count =count + 1

print(" You took " + str(count)+ "steps to guess the number")
print("Coumpter took "+ str(coumpterGuess(0,100,randnum)) + "steps!")



















    