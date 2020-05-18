#imports
import random
#Opening Dialogue
print("Welcome to Blackjack!")

#variable assignment
game = 1
cards = (1,2,3,4,5,6,7,8,9,10,10,10,10,11)
playercard1 = random.choice(cards)
playercard2 = random.choice(cards)
dealercard1 = random.choice(cards)
dealercard2 = random.choice(cards)
playerhand = playercard1 + playercard2

print(f"Your opening hand is {playercard1} and {playercard2} for a total of {playerhand}. The dealer is showing {dealercard1}.")
if playerhand == 21:
	print("BLACKJACK! You win automatically!")
	game = 0

print("Would you like to hit or stay?")
while game == 1:
	hitcard = random.choice(cards)
	playerinput = input()
	
	if playerinput == 'hit':
		playerhand = playerhand + hitcard
		print(f"You drew a {hitcard}, your hand is now worth {playerhand}.") 
		
		if playerhand > 21:
			print("BUST! Better luck next time.")
			game = 0
		else: print("Would you like to hit or stay?")
 
		


	elif playerinput == 'stay':
		

		dealerhand = dealercard1 + dealercard2 #establishes dealerhand value
		
		print(f"Okay, let's see what the dealer has. Remember the dealer always hits on 15. Looks like the dealer has {dealercard1} and {dealercard2} for a total of {dealerhand}") #Dialogue

		if dealerhand > playerhand:
			print("Bummer, looks like the dealer took this one.")
			game = 0

		while game == 1:
			hitcard = random.choice(cards)
			if dealerhand <= 15: 
				dealerhand = dealerhand + hitcard
				print(f"The dealer drew {hitcard}, their total is now {dealerhand}")
			if dealerhand > 21:
				print("The dealer bust! You win!")
				game = 0
			if 22 > dealerhand > playerhand :
				print("Bummer, looks like the dealer took this one. Better luck next time.")
				game = 0
			if 15 < dealerhand < playerhand:
				print("Congrats, you beat the dealer!")
				game = 0
			if dealerhand == playerhand:
				print("A tie! You get to split the pot.")
				game = 0
			
			

		
				
					
					
					
					





