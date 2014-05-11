# Name: guessingGame.py
# Author: Kenneth Hunter
# Date: May 10th, 2014
# Revision: 1.0
# Purpose: A simple guessing game in Python
#-----------------------------------------
import random

maxGuess = 10
number = random.randint(1, 100) #Genrates Num (1-100)

print 'Guess my number from (1-100): '

while maxGuess != 0:

	guessMade = int(raw_input('Insert Guess: '))

	maxGuess -= 1

	print 'You have {0} guesses left'.format(maxGuess)

	# Checks value, and returns to the user if too high or low

	if guessMade < number:
		print 'Your guess is too low!!!'
	
	if guessMade > number:
		print 'Your guess is too high!!'

	if guessMade == number:
		break

# Exits loop, tells user if they won or not
if guessMade == number:
	timesGuess = 10 - maxGuess
	print 'You got it!!!, on try number #{0}'. format(timesGuess)
else: 
	print 'You lost... haha it was {0}'.format(number)






