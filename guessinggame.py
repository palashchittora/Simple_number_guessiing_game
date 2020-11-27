#guessing game
print("Welcome to this fun game. \nThe rules are as follows:\n1. A random number from 1 to 100 will be picked up and you will have to guess it correctly.\n2. If your guess is within range of 10 numbers to the actual number, the system will prompt 'WARM!', if it is not close, the system will promt 'COLD!'.\n3. On subsequent turns, if a guess is closer than the previous guess, the system will prompt 'Warmer!' and otherwise 'Colder!'.\n4. When the guess will match, you will win and the No. of guesses you took will be shown.")
#importing random integer in range 1-100
from random import randint
random_integer=randint(1,100)
#creating list to store guesses
guesses=[0]
while True:
	guess=int(input("Enter your guess: "))
	if guess<1 or guess>100:
		print("OUT OF BOUNDS! Please try again: ")
		continue
	#comparing numbers now
	if guess==random_integer:
		print("Congratulations! you have guessed the number correctly in {} guesses!!".format(len(guesses)))
		break
	guesses.append(guess)
	if guesses[-2]:
		if abs(random_integer-guess) < abs(random_integer-guesses[-2]):
			print('WARMER!')
		else:
			print('COLDER!')
	else:
		if abs(random_integer-guess) <= 10:
			print('WARM!')
		else:
			print('COLD!')