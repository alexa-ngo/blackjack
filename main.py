from deck import Deck
from game import Game
from player import Player

def start_game():

    is_game_running = True

    deck = Deck()
    game = Game()

    # Make and shuffle deck
    deck.make_initial_deck()
    shuffled_deck = deck.shuffle()

    # Player cards
    player_card1 = deck.deal_card()
    player_card2 = deck.deal_card()

    # Dealer cards
    dealer_card1 = deck.deal_card()
    dealer_card2 = deck.deal_card()

    print("\n------------ BlackJack ------------\n")
    print(f"The goal is to get a higher hand value \nthan the dealer without going over 21.\n")
    print(f"Cards from 2 to 10 are worth their face value. \n Jack, Queen, and King are each worth 10. \n While Ace is worth 1.\n")

    print("Shuffling deck... \n")
    game.set_deck(shuffled_deck)

    # Start game with username
    player_name = input("Please enter player name: ")
    game.set_player_name(player_name)
    print(f"Hi, {player_name}!\n")

    # See the cards in the player's hands
    player = Player(shuffled_deck)
    player.set_card(player_card1)
    player.set_card(player_card2)
    print(f"Player's first card: {player_card1[0]}")

    # Show one card in the dealer's hand
    dealer = Player(shuffled_deck)
    dealer.set_card(dealer_card1)
    dealer.set_card(dealer_card2)
    print("Dealer's first card: [FLIPPED OVER]\n")

    # See both cards in the player's hand
    print("Player's cards:")
    player.print_player_hand(player)

    # Show the second card in the dealer's hand
    print("\nDealer's first card: [FLIPPED OVER]")
    print("Dealer's second card: ", dealer_card2[0])

    # Calculate the player's total value
    player_total_sum = player.sum_player_total()
    popped_card = deck.deal_card()
    hit_result = player.do_you_want_to_hit(player_total_sum, popped_card)

    if hit_result == 1:
        popped_card2 = deck.deal_card()
        hit_result = player.do_you_want_to_hit(player_total_sum, popped_card2)

    # The player stands
    if hit_result == 0:
        print("\nPlayer's Cards:")
        player.print_player_hand(player)

        print("\nDealer's Cards:")
        dealer.print_player_hand(dealer)

    # Player folded or lost so the dealer wins
    if hit_result == -1:
        print("You lost!")
        game.set_winner("Dealer")
        is_game_running = False

    # Allow the dealer to hit if their value is less than 16 and when the game is not over.
    if is_game_running is True:
        if dealer.sum_player_total() < 16 and game.get_is_game_over() == False:
            print("\nNow Dealer, since you have less than 16, would you like to hit, fold, or stay? (h/f/s) ")
            game.set_current_player_name("Dealer")
            popped_card = deck.deal_card()
            dealer.do_you_want_to_hit(dealer.sum_player_total(), popped_card)

    print("\n------------ RESULTS ------------\n")
    print(">> Player's Hand:")
    player.print_player_hand(player)
    print(f"Player's sum: {player.sum_player_total()}\n")

    print(">> Dealer Hand:")
    dealer.print_player_hand(dealer)
    print(f"Dealer's sum: {dealer.sum_player_total()}\n")

    if player.sum_player_total() > 21:
        game.set_winner("Dealer")
        print("The Dealer is the winner!\n")
    if dealer.sum_player_total() > 21:
        game.set_winner(game.get_player_name())
        print(f"The {game.get_winner()} is the winner!\n")

    if player.sum_player_total() <= 21:
        game.set_winner(game.get_player_name())
        if player.sum_player_total() > dealer.sum_player_total():
            print(f"The {game.get_winner()} is the winner!\n")
        if player.sum_player_total() < dealer.sum_player_total() <= 21:
            game.set_winner("Dealer")
            print(f"{game.get_winner()} wins!\n")
        if player.sum_player_total() == dealer.sum_player_total():
            print("There's a tie!\n")
            decision = input("Would you like to play again? (y/n) ... ").lower()
            if decision == "y":
                start_game()
            else:
                print("See you soon!\n\n")

    print("--------------------------------\n")
    response = input("Would you like to play again? (y/n) ... ")
    if response == 'y':
        start_game()
    else:
        print("See you soon!\n\n")

start_game()