from player import Player
import random

class War:

    def __init__(self):
        self.player_1 = Player(name="Player 1")
        self.player_2 = Player(name="Player 2")
        self.winner = None
        self.__initialize_game()

    def __initialize_game(self):
        random_deck = self.__generate_random_deck()
        for i in range(len(random_deck)):
            if i % 2 == 0:
                self.player_1.insert_card(random_deck[i])
            else:
                self.player_2.insert_card(random_deck[i])
        print(len(self.player_1.deck))
        print(len(self.player_2.deck))        

    def __generate_random_deck(self):
        # A = 1, 2-10, J = 11, Q = 12, K = 13
        single_face = [x for x in range(1,14)]
        deck = single_face + single_face + single_face + single_face
        random.shuffle(deck)
        return deck

    def __check_for_winner(self):
        if not self.player_1.can_draw:
            self.winner = self.player_2
        if not self.player_2.can_draw:
            self.winner = self.player_1

    def take_turn(self):
        self.flip_card(winnings=[])

    def flip_card(self, winnings):
        self.__check_for_winner()
        if self.winner:
            return
            
        c1 = self.player_1.draw_card()
        c2 = self.player_2.draw_card()

        print("PLAYER 1 CARD: {}, PLAYER 2 CARD: {}".format(c1, c2))

        winnings += [c1, c2]
        random.shuffle(winnings)

        if c1 > c2:
            print("PLAYER 1 WINS {} CARDS".format(len(winnings)))
            [self.player_1.insert_card(card) for card in winnings]
        elif c1 < c2:
            print("PLAYER 2 WINS {} CARDS".format(len(winnings)))
            [self.player_2.insert_card(card) for card in winnings]
        else:
            print("GOES TO WAR")
            self.play_war(winnings)
        # check incase last play ended game
        self.__check_for_winner()

    def play_war(self, winnings):
        if not self.player_1.can_war:
            self.winner = self.player_2
            return
        if not self.player_2.can_war:
            self.winnder = self.player_1
            return 

        # each player needs to sacrafice two cards to the pot
        for _ in range(2):
            winnings.append(self.player_1.draw_card())
            winnings.append(self.player_2.draw_card())

        self.flip_card(winnings)
