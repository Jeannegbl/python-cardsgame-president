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
    for i in range(len(g.players)):
        g.players[i].ordre = i
    tour = 0

    wanna_continue = True
    while wanna_continue:
        choix = ""
        choice = "3"
        nb_cards = 0
        last_player = "You"
        while tour < len(g.players) - 1:
            for i in range(len(g.players)):
                print(g.players[i].name, ":", len(g.players[i].hand), "cartes")

            print('Your current deck is : ')
            print(g.main_player.hand, )
            print_ln()

            choix = input('What value do you wish to play ? ')

            while choix < choice:
                if choix == "0" or choix == "10" or choix == "2" or nb_cards == 0:
                    break
                choix = input('What value do you wish to play ? ')


            if choix == "0":
                plays = g.main_player.play([])
                tour = tour + 1
            else:
                choice = choix
                plays = g.main_player.play(choice)
                tour = 0
                last_player = "You"

            print(f"You play {plays}")
            if len(plays) == 0 and nb_cards == 0:
                nb_cards = 1
            elif len(plays) == 0 and nb_cards > 0:
                nb_cards = nb_cards
            else:
                nb_cards = len(plays)

            for ai in g.ai_players:
                if tour == len(g.players) - 1:
                    break
                if plays != [] and (choice == "2" or nb_cards == 4):
                    tour = len(g.players) - 1
                    break
                plays = ai.play(choice, nb_cards)
                print(f"{ai.name} plays \t {plays}")
                if plays != [] and (ai.card_valeur == 15 or nb_cards == 4):
                    if len(plays) > 0:
                        choice = plays[0].symbol
                        last_player = ai.name
                        tour = len(g.players) -1
                    break
                if plays == []:
                    tour = tour + 1
                if plays != []:
                    tour = 0

                # Update latest card played
                if len(plays) > 0:
                    choice = plays[0].symbol
                    last_player = ai.name

        if tour == len(g.players) - 1:
            print(f"Le tour est fini : {last_player} commence le tour")
            for i in range(len(g.players)):
                if last_player == g.players[i].name:
                    after_last_player = i+1
                    after_after_last_player = i+2
                    g.players[i].ordre = 0
                    if i+1 > 3:
                        after_last_player = 0
                    g.players[after_last_player].ordre = 1
                    if i+2 == 4:
                        after_after_last_player = 0
                    if i+2 == 5:
                        after_after_last_player = 1
                    g.players[after_after_last_player].ordre = 2
                    g.players[i-1].ordre = 3
                    for i in range(len(g.players)):
                        print(g.players[i].name, ":", len(g.players[i].hand), "cartes")

            tour = 0
            choix = ""
            choice = "3"
            nb_cards = 1
            last_player = "You"
            while tour < len(g.players) - 1:
                for i in range(len(g.players)):
                    if tour == len(g.players) - 1:
                        break
                    if g.players[i].ordre == 0:
                        if i == 0:
                            print('Your current deck is : ')
                            print(g.main_player.hand, )
                            choix = input('What value do you wish to play ? ')

                            while choix < choice:
                                if choix == "0" or choix == "10" or choix == "2":
                                    break
                                choix = input('What value do you wish to play ? ')

                            if choix == "0":
                                plays = g.main_player.play([])
                                tour = tour + 1
                            else:
                                choice = choix
                                plays = g.main_player.play(choice)
                                tour = 0
                                last_player = "You"

                            print(f"You play {plays}")
                            if len(plays) == 0 and nb_cards == 0:
                                nb_cards = 1
                            elif len(plays) == 0 and nb_cards > 0:
                                nb_cards = nb_cards
                            else:
                                nb_cards = len(plays)
                        else:
                            if plays != [] and (choice == "2" or nb_cards == 4):
                                tour = len(g.players) - 1
                                last_player = "You"
                                break
                            plays = g.players[i].play(choice, nb_cards)
                            print(f"{g.players[i].name} plays \t {plays}")
                            if plays != [] and (g.players[i].card_valeur == 15 or nb_cards == 4):
                                if len(plays) > 0:
                                    choice = plays[0].symbol
                                    last_player = g.players[i].name
                                    tour = len(g.players) - 1
                                break
                            if plays == []:
                                tour = tour + 1
                            if plays != []:
                                tour = 0
                                last_player = g.players[i].name
                            if len(plays) > 0:
                                choice = plays[0].symbol
                        for j in range(len(g.players)):
                            if tour == len(g.players) - 1:
                                break
                            if g.players[j].ordre == 1:
                                if j == 0:
                                    print('Your current deck is : ')
                                    print(g.main_player.hand, )
                                    choix = input('What value do you wish to play ? ')

                                    while choix < choice:
                                        if choix == "0" or choix == "10" or choix == "2":
                                            break
                                        choix = input('What value do you wish to play ? ')

                                    if choix == "0":
                                        plays = g.main_player.play([])
                                        tour = tour + 1
                                    else:
                                        choice = choix
                                        plays = g.main_player.play(choice)
                                        tour = 0
                                        last_player = "You"

                                    print(f"You play {plays}")
                                    if len(plays) == 0 and nb_cards == 0:
                                        nb_cards = 1
                                    elif len(plays) == 0 and nb_cards > 0:
                                        nb_cards = nb_cards
                                    else:
                                        nb_cards = len(plays)
                                else:
                                    if plays != [] and (choice == "2" or nb_cards == 4):
                                        tour = len(g.players) - 1
                                        last_player = "You"
                                        break
                                    plays = g.players[j].play(choice, nb_cards)
                                    print(f"{g.players[j].name} plays \t {plays}")
                                    if plays != [] and (g.players[j].card_valeur == 15 or nb_cards == 4):
                                        if len(plays) > 0:
                                            choice = plays[0].symbol
                                            last_player = g.players[j].name
                                            tour = len(g.players) - 1
                                        break
                                    if plays == []:
                                        tour = tour + 1
                                    if plays != []:
                                        tour = 0
                                        last_player = g.players[j].name
                                    if len(plays) > 0:
                                        choice = plays[0].symbol
                                for k in range(len(g.players)):
                                    if tour == len(g.players) - 1:
                                        break
                                    if g.players[k].ordre == 2:
                                        if k == 0:
                                            print('Your current deck is : ')
                                            print(g.main_player.hand, )
                                            choix = input('What value do you wish to play ? ')

                                            while choix < choice:
                                                if choix == "0" or choix == "10" or choix == "2":
                                                    break
                                                choix = input('What value do you wish to play ? ')

                                            if choix == "0":
                                                plays = g.main_player.play([])
                                                tour = tour + 1
                                            else:
                                                choice = choix
                                                plays = g.main_player.play(choice)
                                                tour = 0
                                                last_player = "You"

                                            print(f"You play {plays}")
                                            if len(plays) == 0 and nb_cards == 0:
                                                nb_cards = 1
                                            elif len(plays) == 0 and nb_cards > 0:
                                                nb_cards = nb_cards
                                            else:
                                                nb_cards = len(plays)
                                        else:
                                            if plays != [] and (choice == "2" or nb_cards == 4):
                                                tour = len(g.players) - 1
                                                last_player = "You"
                                                break
                                            plays = g.players[k].play(choice, nb_cards)
                                            print(f"{g.players[k].name} plays \t {plays}")
                                            if plays != [] and (g.players[k].card_valeur == 15 or nb_cards == 4):
                                                if len(plays) > 0:
                                                    choice = plays[0].symbol
                                                    last_player = g.players[k].name
                                                    tour = len(g.players) - 1
                                                break
                                            if plays == []:
                                                tour = tour + 1
                                            if plays != []:
                                                tour = 0
                                                last_player = g.players[k].name
                                            if len(plays) > 0:
                                                choice = plays[0].symbol
                                        for l in range(len(g.players)):
                                            if tour == len(g.players) - 1:
                                                break
                                            if g.players[l].ordre == 3:
                                                if l == 0:
                                                    print('Your current deck is : ')
                                                    print(g.main_player.hand, )
                                                    choix = input('What value do you wish to play ? ')

                                                    while choix < choice:
                                                        if choix == "0" or choix == "10" or choix == "2":
                                                            break
                                                        choix = input('What value do you wish to play ? ')

                                                    if choix == "0":
                                                        plays = g.main_player.play([])
                                                        tour = tour + 1
                                                    else:
                                                        choice = choix
                                                        plays = g.main_player.play(choice)
                                                        tour = 0
                                                        last_player = "You"

                                                    print(f"You play {plays}")
                                                    if len(plays) == 0 and nb_cards == 0:
                                                        nb_cards = 1
                                                    elif len(plays) == 0 and nb_cards > 0:
                                                        nb_cards = nb_cards
                                                    else:
                                                        nb_cards = len(plays)
                                                else:
                                                    if plays != [] and (choice == "2" or nb_cards == 4):
                                                        tour = len(g.players) - 1
                                                        last_player = "You"
                                                        break
                                                    plays = g.players[l].play(choice, nb_cards)
                                                    print(f"{g.players[l].name} plays \t {plays}")
                                                    if plays != [] and (g.players[l].card_valeur == 15 or nb_cards == 4):
                                                        if len(plays) > 0:
                                                            choice = plays[0].symbol
                                                            last_player = g.players[l].name
                                                            tour = len(g.players) - 1
                                                        break
                                                    if plays == []:
                                                        tour = tour + 1
                                                    if plays != []:
                                                        tour = 0
                                                        last_player = g.players[l].name
                                                    if len(plays) > 0:
                                                        choice = plays[0].symbol
                    if len(g.players[i].hand) == 0:
                        if i == 0:
                            print("Vous avez gagné !!")
                            return
                        else:
                            print("Le joueur", g.players[i].name, "a gagné !!")
                            return

                    if tour == len(g.players) - 1:
                        print(f"Le tour est fini : {last_player} commence le tour")
                        for i in range(len(g.players)):
                            if last_player == g.players[i].name:
                                after_last_player = i + 1
                                after_after_last_player = i + 2
                                g.players[i].ordre = 0
                                if i + 1 > 3:
                                    after_last_player = 0
                                g.players[after_last_player].ordre = 1
                                if i + 2 == 4:
                                    after_after_last_player = 0
                                if i + 2 == 5:
                                    after_after_last_player = 1
                                g.players[after_after_last_player].ordre = 2
                                g.players[i - 1].ordre = 3
                                for i in range(len(g.players)):
                                    print(g.players[i].name, ":", len(g.players[i].hand), "cartes")
                                tour = 0
                                choice = ""
                                nb_cards = 1
                        break


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
