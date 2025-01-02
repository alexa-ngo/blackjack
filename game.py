from deck import Deck
from player import Player

class Game:

    def __init__(self):
        self._curr_deck = None
        self._curr_player_name = None
        self._is_game_over = False
        self._player_name = None
        self._winner = None

    # Setters and Getters
    def get_current_player_name(self):
        return self._curr_player_name

    def set_current_player_name(self, current_player_name):
        self._curr_player_name = current_player_name
        self._winner = current_player_name

    def get_deck(self):
        copied_deck = list(self._curr_deck)
        return copied_deck

    def set_deck(self, deck_of_cards):
        self._curr_deck = deck_of_cards

    def get_is_game_over(self):
        return self._is_game_over

    def set_is_game_over(self):
        self._is_game_over = True

    def get_player_name(self):
        player_name = self._player_name
        return player_name

    def set_player_name(self, input_of_name):
        self._player_name = input_of_name

    def get_winner(self):
        winner = self._winner
        return winner

    def set_winner(self, dealer_or_player):
        self._winner = dealer_or_player
