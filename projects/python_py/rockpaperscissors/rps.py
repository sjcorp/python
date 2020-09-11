#Rock Paper Scissors Game
from random import choice
 
rules = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'} #dictionary containing result combinations in the 'is beaten by' format
options = ['rock', 'paper', 'scissors'] #list containing optinos for the computer
m = 0
u = 0

while True:
	print(
		"""
	\n______________________________________________________
	\nPlay...\n1. Rock\n2. Paper\n3. Scissors\n0. End""")
	    
	human = int(input('\nChoose Your Weapon: '))
	    
	if human == 1:
		user = 'rock'
	elif human == 2:
	  user = 'paper'
	elif human == 3:
	  user = 'scissors'
	else:
	  user = 'to quit'
	 
	print("\nYou Played", user)
	    
	computer = choice(options)  # choose the weapon which beats a randomly chosen weapon from "previous"
	    
	if user == 'to quit':
		break
	elif user in rules:
		print('The Computer Played', computer, end='; ')
	 
	if rules[computer] == user:  # if what beats the computer's choice is the human's choice...
		m += 1
		u += 1
		print('\nYayy You Win!')
		print(f'So far, you have won {u} out of {m} matches with {round(u/m*100,1)}% success rate')
	elif rules[user] == computer:  # if what beats the human's choice is the computer's choice...
		m += 1
		u += 0
		print('\nUh Oh...The computer beat you... :(')
		print(f'So far, you have won {u} out of {m} matches with {round(u/m*100,1)}% success rate')
	else: 
		m += 1
		u += 0
		print("it's a tie!")
		print(f'So far, you have won {u} out of {m} matches with {round(u/m*100,1)}% success rate')
