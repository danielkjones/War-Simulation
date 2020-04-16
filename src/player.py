from collections import deque

class Player:

    def __init__(self, name):
        self.deck = deque()
        self.name = name

    @property
    def can_draw(self):
        return len(self.deck) != 0

    @property
    def can_war(self):
        return len(self.deck) >= 3

    def insert_card(self, card):
        self.deck.insert(0, card)

    def draw_card(self):
        return self.deck.pop()

    def reset_player(self):
        self.deck.clear()
