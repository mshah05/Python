'''
Author: Mansi Shah
'''
import random

card_suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
card_rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'K': 10, 'Q': 10, 'J': 10}
used_cards = []
		
class Card(object):
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	def print_card(self):
		print "New card added to hand: ", self.rank + ' of ' + self.suit
	def get_card_value(self, current_hand_value):
		card_value = 0
		if self.rank == 'Ace':
			if current_hand_value <= 10:
				card_value = 11
			else:
				card_value = 1
		else:
			card_value = card_values[self.rank];
		return card_value 
		
class Hand(object):
	def __init__(self):
		self.cards = []
		self.hand_value = 0
	def get_hand_value(self):
		return self.hand_value
	def check_hand_value(self):
		if self.hand_value > 21:
			print "Busted! Hand value is: " + self.hand_value
		elif self.hand_value == 21:
			print "Current hand value is 21."
	def add_card_player(self):
		new_card = Card(card_rank[random.randint(0, 12)], card_suit[random.randint(0, 3)])
		new_card_str = new_card.rank + " of " + new_card.suit
		#ensuring that we do not pick the same card twice since we are only using one deck per game
		while new_card_str in used_cards:
			new_card = Card(card_rank[random.randint(0, 12)], card_suit[random.randint(0, 3)])
			new_card_str = new_card.rank + " of " + new_card.suit
		new_card.print_card()
		self.cards.append(new_card)
		used_cards.append(new_card_str)
		self.hand_value = self.hand_value + new_card.get_card_value(self.hand_value)
		print "Current value of hand: ", self.hand_value, "\n"
	'''
	The difference between add_card_player and add_card_dealer is that the dealer's cards are not shown on the screen
	when they are dealt; this is specifically for the first 2 cards that are dealt at the beginning of the game
	'''
	def add_card_dealer(self):
		new_card = Card(card_rank[random.randint(0, 12)], card_suit[random.randint(0, 3)])
		new_card_str = new_card.rank + " of " + new_card.suit
		#ensuring that we do not pick the same card twice since we are only using one deck
		while new_card_str in used_cards:
			new_card = Card(card_rank[random.randint(0, 12)], card_suit[random.randint(0, 3)])
			new_card_str = new_card.rank + " of " + new_card.suit
		self.cards.append(new_card)
		used_cards.append(new_card_str)
		self.hand_value = self.hand_value + new_card.get_card_value(self.hand_value)
	def show_hand(self):
		for c in self.cards:
			print c.rank, 'of', c.suit
		
class Player(object):
	def __init__(self):
		self.player_hand = Hand()
	
def player_has_blackjack(value):
	if value == 21:
		print "Congratulations you have blackjack! You win this game!"
		return True
	else:
		return False
		
def play_game():
	human_busted = False
	dealer_busted = False 
	
	#deck shuffled before the game
	random.shuffle(card_suit)
	random.shuffle(card_rank)
	
	human = Player()
	dealer = Player()
	
	#both players dealt 2 cards at the start of the game
	#The human player's cards are shown on screen, the dealers are not.
	print "\nDealing the first 2 cards to start off the game: \n"
	
	human.player_hand.add_card_player()
	human.player_hand.add_card_player()
	
	dealer.player_hand.add_card_dealer()
	dealer.player_hand.add_card_dealer()
	
	if human.player_hand.get_hand_value() == 21 and dealer.player_hand.get_hand_value() == 21:
		print "Dealer's hand: "
		dealer.player_hand.show_hand()
		print "\nFinal Decision: There is a tie. Both yours and dealer's hand equal 21.\n"
		print "\nEnd of this game.\n"
	elif human.player_hand.get_hand_value() == 21:
		print "\nFinal Decision: You win!! The value of your hand is 21.\n" 
		print "\nEnd of this game.\n"
	#Dealer's hand value is also evaluated after the first 2 cards are dealt. If this is not desired, the following elif
	#set of statements can be removed.
	elif dealer.player_hand.get_hand_value() == 21:
		print "Dealer's hand: "
		dealer.player_hand.show_hand()
		print "\nFinal Decision: Dealer wins this game! The value of their hand is 21.\n"
		print "\nEnd of this game.\n" 
	else:
		#The player plays their turn
		print "Your turn:"
		deal_or_not = raw_input("Would you like to be dealt another card?  Y or N? ")
		while deal_or_not != "Y" and deal_or_not != "y" and deal_or_not != "N" and deal_or_not != "n":
			deal_or_not = raw_input("Please input a correct answer: Y or N?: ")
			print "\n"
		while(deal_or_not == "Y" or deal_or_not == "y"):
			human.player_hand.add_card_player()
			'''
			If the new card added puts human player's hand at 21, they automatically win and the game is over.
			If dealer should still get their turn, the next 2 lines (line 1 and 2) can be commented out.
			'''
			if player_has_blackjack(human.player_hand.get_hand_value()): #line 1
				return #line 2
			if human.player_hand.get_hand_value() > 21:
				print "BUSTED! Your hand value is over 21 so your turn is over!\n"
				human_busted = True
				break
			else:
				deal_or_not = raw_input("Would you like to be dealt another card? Y or N? ")
				while deal_or_not != "Y" and deal_or_not != "y" and deal_or_not != "N" and deal_or_not != "n":
					deal_or_not = raw_input("Please input a correct answer: Y or N?: ")
	
		#The dealer plays their turn
		print "\nDealer's turn.\n"
		print "Dealer's Hand: "
		dealer.player_hand.show_hand()
		while dealer.player_hand.get_hand_value() < 17:
			print "\nThe dealer hits.\n"
			dealer.player_hand.add_card_player()
			print "Dealer's Hand: "
			dealer.player_hand.show_hand()
		if dealer.player_hand.get_hand_value() > 21:
			print "\nDealer is busted, their turn is over!\n"
			dealer_busted = True
		else:
			print "\nThe dealer chooses to stand.\n"
		
		#Making the final decision for the game: 
		dealer_hand = dealer.player_hand.get_hand_value()
		player_hand = human.player_hand.get_hand_value()
		print "Total value of dealer's hand: ", dealer_hand
		print "Total value of your hand: ", player_hand
		if dealer_busted and human_busted:
			print "\nFinal Decision: Both players have busted, the dealer wins this game!"
			return
		if player_hand == dealer_hand:
			print "\nFinal Decision: It is a tie! No one wins this game!\n"
		elif dealer_hand > player_hand and dealer_busted == False:
			print "\nFinal Decision: Dealer wins this game!\n"
		elif player_hand < dealer_hand and dealer_busted:
			print "\nFinal Decision: You win this game!\n"
		elif player_hand > dealer_hand and human_busted == False:
			print "\nFinal Decision: You win this game!\n"
		elif player_hand > dealer_hand and human_busted:
			print "\nFinal Decision: Dealer wins this game!\n"
	
	
def main():
	play_game()
		
		
main()