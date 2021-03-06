### Table of Contents:
    A. Game Summary and Outline
    B. Notes
    C. Instructions
    
### A. Game Summary and Outline
Blackjack is a game often played in casinos around the world. It is played between only 2 players - yourself and the dealer at the table. The goal of the game is to have a hand value as close to or equal to 21 without going over. The value of each player's (yourself and the dealer) hand is evaluated using the value of the individual cards in the player's hand. Each card counts as their face value, except for Ace which can count as 1 or 11, and K, Q, and J are counted as 10. If a player scores 21, they win the game. Otherwise, the player with the higer hand value, that's still below 21, wins. Players can tie if both of their hand values are equal or bust if their individual hand value goes over 21.

  **General game flow:**  
          1. Two cards are dealt to each player at the start of the game. The value of each player's hand is evaluated. If neither player's hand value is 21, the game continues.  
	  2. Human player takes their turn.  
	  3. Dealer plays their turn.   
	  4. A final decision is made based on the value of both player's hands.  

### B. Notes:
Below are some cautionary notes to keep in mind: 
1. **This code calls for Python 3 to be installed on the machine that is running it.**
2. The human player is the person running the program so it is not automated. 
3. The dealer is automated.
4. If the human player's first 2 cards equal 21, they automatically win the game and the dealer does not get a turn. 
		  _This feature can be removed if desired. Please see comments in the source file inside the play_game() method._  
5. Human player's first 2 cards, dealt at the beginning of the game, are shown on screen, dealer's are not. 
6. When the dealer plays, if he hits, the new card added as well as his hand, are shown on screen.
7. During the human player's turn if the next card dealt to them puts their hands' value at 21, they win and the game is over and the dealer does not play. 
		  _If this is not desired, and the dealer should still get their turn, then only two lines of code in the source file         need to be commented to remove this feature. Please see comments in the play_game() method._  
8. The dealer still gets their turn even if the human player's hand is busted.
9. If the total value of either player's hand is less then or equal to 10 before an Ace is dealt, the Ace will count as 
	11, otherwise it will count as 1.
10. Both player's hands is evaluated after the first 2 cards are dealt and a decision is made either declaring a winner or continuing with the game. This means the dealer's cards are also evaluated after the first 2 cards are dealt and if they get 21, they win.
		  _This feature can be removed if desired. Please see comments in source file inside the play_game() method._  
11. If both players tie, no one wins the game.

### C. Instructions:
The game source code is contained in blackjack.py which can be run through the windows command prompt.

Through the command prompt, please navigate to where the source file is located or downloaded on your computer and type "python blackjack.py" to run the program. Follow the instructions given on screen to play the game.
