from deck import Deck

class Player:

    def __init__(self, deck):
        self._deck = deck
        self._player_hand_arr = []
        self._player_total = 0

    # Setters and Getters

    def get_player_total(self):
        player_pot_total = self._player_total
        return player_pot_total

    def set_player_total(self, amount):
        self._player_total += amount

    def set_card(self, card: tuple):
        self._player_hand_arr.append(card)
        return

    def copy_of_player_hand_array(self):
        player_hand_list = []
        for card in self._player_hand_arr:
            player_hand_list.append(card)
        return player_hand_list

    def do_you_want_to_hit(self, player_sum, popped_card):

        decision = input("\nhit, fold, or stand? (h/f/s) ")
        response = decision.lower()

        if response == "h":
            print("\nPopped card:          >> ", popped_card[1])
            self._player_hand_arr.append(popped_card)
            self.set_player_total(popped_card[1] + player_sum)
            print("Current player's hand: ")
            self.print_player_hand(self)
            print("\nTotal: ", self.get_player_total())
            if self._player_total > 21:
                print("Game Over! ")
                return -1

        if response == "f":
            print("You have folded")
            return -1

        if response == "s":
            print("Stand and do nothing with the cards")
            return 0

        return 1

    def print_player_hand(self, dealer_or_player):
        player_hand_list = self.copy_of_player_hand_array()

        for value in range(len(player_hand_list)):
            print(f"\t{player_hand_list[value][0]}")

    def sum_player_total(self):
        player_hand_list = self.copy_of_player_hand_array()
        total_sum = 0

        for card in player_hand_list:
            total_sum += card[1]

        return total_sum