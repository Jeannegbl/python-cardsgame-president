from models import PresidentGame


def print_ln():
    print('\n')


def game_loop(g: PresidentGame):
    """
    The main game loop.
    Loops in circle until the user wants to quit the application.
    Args:
        g: The President Game instance.
    """

    wanna_continue = True
    while wanna_continue:

        for i in range(len(g.players)):
            print(g.players[i].name, ":", len(g.players[i].hand), "cartes")

        print('Your current deck is : ')
        print(g.main_player.hand, )
        print_ln()
        choice = '0'

        while g.main_player.has_symbol(choice) == 0:
            choice = input('What value do you wish to play ? ')

        plays = g.main_player.play(choice)

        print(f"You play {plays}")
        nb_cards = len(plays)
        best_card = choice
        for ai in g.ai_players:
            if plays != [] and (choice == "2" or nb_cards == 4):
                break
            plays = ai.play(choice, nb_cards)
            print(f"{ai.name} plays \t {plays}")
            if plays != [] and (ai.card_valeur == 15 or nb_cards == 4):
                if len(plays) > 0:
                    choice = plays[0].symbol
                ai.remove_from_hand(plays)
                break
            ai.remove_from_hand(plays)

            # Update latest card played
            if len(plays) > 0:
                choice = plays[0].symbol
        print(choice)

        for i in range(len(g.players)):
            if len(g.players[i].hand) == 0:
                if i == 0:
                    print("Vous avez gagné !!")
                    return
                else:
                    print("Le joueur", g.players[i].name, "a gagné !!")
                    return

        wanna_continue = input('Do you want to continue playing (y/N)? ')
        wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')




if __name__ == '__main__':
    print_ln()
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    g = PresidentGame()
    game_loop(g)
    print('Thank you for playing. I hope you enjoyed !')
