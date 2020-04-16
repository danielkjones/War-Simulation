from war import War
import sys

LOG_FILE = "../data/game_log.csv"

def game_driver(iterations=1):
    completed_iterations = 0
    w = War()
    while completed_iterations < iterations:
        game_in_session = True
        w.reset_game()
        while game_in_session:
            print('CURRENT DECK')
            print('PLAYER 1 DECK: \n{}, \n# CARDS: {}'.format(w.player_1.deck, len(w.player_1.deck)))
            print('PLAYER 2 DECK: \n{}, \n# CARDS: {}'.format(w.player_2.deck, len(w.player_2.deck)))
            # _ = input('CLICK FOR TURN NUMBER {}'.format(turns))
            print('PLAYING TURN # {}'.format(w.turns_of_play))
            w.take_turn()
            game_in_session = w.winner == None
        print("TOTAL TURNS FOR THIS GAME: {}\n" \
            "TOTAL WAR HANDS FOR THIS GAME: {}\n" \
            "WINNER: {}".format(w.turns_of_play, w.war_hands, w.winner.name))
        log_results(w.turns_of_play, w.war_hands, w.winner.name)
        completed_iterations += 1

def log_results(total_turns, war_hands, winner):
    with open(LOG_FILE, "a") as f:
        f.write("{},{},{}\n".format(total_turns, war_hands, winner))

if __name__ == "__main__":
    game_iterations = 1
    if len(sys.argv) >= 2:
        game_iterations = int(sys.argv[1])
    game_driver(iterations=game_iterations)
