from war import War

def game_driver():
    game_in_session = True
    w = War()
    turns = 0
    while game_in_session:
        turns += 1
        print('CURRENT DECK')
        print('PLAYER 1 DECK: \n{}, \n# CARDS: {}'.format(w.player_1.deck, len(w.player_1.deck)))
        print('PLAYER 2 DECK: \n{}, \n# CARDS: {}'.format(w.player_2.deck, len(w.player_2.deck)))
        # _ = input('CLICK FOR TURN NUMBER {}'.format(turns))
        print('PLAYING TURN # {}'.format(turns))
        w.take_turn()
        game_in_session = w.winner == None
    print("TOTAL TURNS FOR THIS GAME: {}, WINNER IS {}".format(turns, w.winner.name))
    print("(game counted total turns: {}, game counted war turns {})".format(w.turns_of_play, w.war_hands))

if __name__ == "__main__":
    game_driver()
        
