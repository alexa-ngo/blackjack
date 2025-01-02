import random

class Deck:

    def __init__(self):
        self._deck = []

    def __iter__(self):
        """
        Iterates through each tuple of the deck
        """
        self.curr_deck_idx = 0
        self.deck_to_iterate = list(self._deck)
        return

    def __next__(self):
        if self.curr_deck_idx < len(self.deck_to_iterate):
            curr_result = self.deck_to_iterate[self.curr_deck_idx]
            self.curr_deck_idx += 1
            return curr_result

        raise StopIteration

    # Getters and Setters
    def get_curr_deck(self):
        """
        Returns a copy of the current deck.
        """
        idx = 0
        result = []
        for card in self._deck:
            result.append(card)
            idx += 1
        return result

    def set_curr_deck(self, deck):
        self._deck = deck

    def deal_card(self):
        """
        Returns the first card on top of the current deck.
        """
        return self._deck.pop()

    def make_initial_deck(self):
        """
        Creates the initial deck.
        """
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace'] * 4

        for card in cards:
            if type(card) == int:
                card_and_value = (card, card)
                self._deck.append(card_and_value)
            elif card == 'jack' or card == 'queen' or card == 'king':
                card_and_value = (card, 10)
                self._deck.append(card_and_value)
            elif card == 'ace':
                card_and_value = (card, 1)
                self._deck.append(card_and_value)

        return self._deck

    def print_deck(self):
        idx = 0
        for card in self._deck:
            print(f"{card}")
            idx += 1
        return

    def shuffle(self):
        """
        Shuffles the deck.
        """
        random.shuffle(self._deck)
        return self._deck