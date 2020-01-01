#Author: Syed Farhan Ahmed 

import sys
import random

#with open allows file to closed after reading automatically
def setupList():
	textFile = sys.argv[1]
	wordList = []	
	with open(textFile, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			wordList.append(line)
	return wordList
    

def selectRandomword():
	wordList = setupList()
	while True:
		randomdWord = random.choice(wordList)
		if len(randomdWord) >= 4:
			return randomdWord
	

def userInput(): 
	while True:
		userI = input("What's your guess?: ")
		if len(userI) == 1 and not userI.isdigit() and not userI.isspace():
			return userI.lower()
		else:
			print('Invalid input, please try again.')


def secretWord():
	hiddenChar = ' _ '
	secretWord = [] 
	randomdWord = selectRandomword()
	for i in range(len(randomdWord)):
		secretWord += [hiddenChar,] 
	return {'wordhidden': secretWord, 'word': randomdWord} 


def gameMain(): 
	print('Welcome to the game of Hangman!')
	secretWordreturn = secretWord()
	wordHidden = secretWordreturn['wordhidden']
	wordActual = secretWordreturn['word']
	wordActuallist = list(wordActual)
	charGuessedsofar = " "
	num_guesses = 8
	
	while True:
		
		wordHiddenstr = ' '.join(wordHidden)
		print('\nThe secret word looks like: ', wordHiddenstr)
		
		if num_guesses != 1:
			print('You have {} guesses remaining'.format(num_guesses))
		else:
			print('You have {} remaining guess'.format(num_guesses))	
		print('Unsuccessful guesses so far:',charGuessedsofar.rstrip(','))

		if num_guesses != 0:
			userI = userInput()
		else:
			print('Game over,no more guesses left.')
			print("The word is '{}' ".format(wordActual))
			break

		#start of comment:FIRST checks for word if already guessed or not, then checks for index wordActuallist with userinput, if they're same it replaces that index for wordhidden with blank ' _ ' for word userinput 
		if userI in wordHidden:
			print('already guessed, try something new.')
		elif userI in wordActuallist:
			print('Nice guess!')
			for i in range(len(wordActuallist)):
				if wordActuallist[i] == userI:
					wordHidden[i] = userI
		

		#if character not present in sceret word, reduce number of guesses by -1 for every user input, and print messages regarding it 
		if userI not in wordActual:
			print("Sorry there is no '{}'".format(userI))
			#checks for double inputs prompts user to input again
			if userI in charGuessedsofar:
				print('already guessed, try something new.')
			else:
				num_guesses = num_guesses - 1
				charGuessedsofar += userI + ' '
		
		#if all '_' (character) are replaced  then the word is guessed correctly and hence rthe word is revealed.
		if ' _ ' not in wordHidden:
			wordHidden = ''.join(wordHidden)
			print('Congratulations!\nyou guessed the correct word: {}'.format(wordHidden))
			break
		
	
gameMain()
