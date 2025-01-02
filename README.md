# 24-7 BlackJack Game ♠️♥️♣️♦️ 

This is a simple text console-based Python implementation of the Blackjack game which is also known as 21! 

### How to Start Playing
This game requires Python3, and we don't need any other dependencies besides the Python Standard Library.

We simply start the game with:
```commandline
$ python3 main.py
```
The goal of BlackJack is to get a higher hand value than the dealer without going over 21. 

The cards from 2 to 10 are worth their face value. Jack, Queen, and King are each worth 10 points, 
while Ace is worth 1 point. The player can either choose between hit, fold, or stand in an attempt to beat the Dealer.
The goal is to have the cards in the hand add up to 21 points and without going over it, 
while at the same time having a value greater than the Dealer.

Here is an example of how the game looks like:
```
Hi, Alexa!

Player's first card: 7
Dealer's first card: [FLIPPED OVER]

Player's cards:
        7
        10

Dealer's first card: [FLIPPED OVER]
Dealer's second card:  7

hit, fold, or stand? (h/f/s) s
Stand and do nothing with the cards

Player's Cards:
        7
        10

Dealer's Cards:
        9
        7

------------ RESULTS ------------

>> Player's Hand:
        7
        10
Player's sum: 17

>> Dealer Hand:
        9
        7
Dealer's sum: 16

The Alexa is the winner!

--------------------------------
```

Yeah, it's easy as that! Have fun playing 24-7 BlackJack! 😎 ♠️♥️♣️♦️ 