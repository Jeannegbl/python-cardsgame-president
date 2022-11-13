import tkinter

from models import PresidentGame, Affichage
from tkinter import *

def print_ln():
    print('\n')


def init_tk():
    self = Tk()
    self.title('Le président')
    self.geometry("1680x1050")
    self.configure(bg='green')

def game_loop(g: PresidentGame):
    """
    The main game loop.
    Loops in circle until the user wants to quit the application.
    Args:
        g: The President Game instance.
    """
    init_tk()
    for i in range(len(g.players)):
        g.players[i].ordre = i
        g.players[i].finish = 0
        g.players[i].role = ""
        g.players[i].score = 0
    last_player = "You"
    g.nb_partie = 0

    wanna_continue = True
    while wanna_continue:
        #Ici on creer la boucle qui en fonction du role en fin de partie donne une carte aux role concerner
        for i in range(len(g.players)):
            if g.players[i].role == "Président":
                president = g.players[i]
            if g.players[i].role == "Trouduc":
                trouduc = g.players[i]
        for i in range(len(g.players)):
            if g.players[i].role == "Président":
                if i == 0:
                    print(g.players[i].hand)
                    random_card = input("Donner une carte au Trouduc")
                    g.players[i].give_president(random_card, trouduc, g.main_player.hand)
                    g.players[i].remove_give_president(random_card, g.main_player.hand)
                else:
                    random_card = g.players[i].hand[0]
                    g.players[i].give(random_card, trouduc)
                    g.players[i].remove_give(random_card)
            if g.players[i].role == "Trouduc":
                last_card = g.players[i].hand[-1]
                g.players[i].give(last_card, president)
                g.players[i].remove_give(last_card)


        tour = 0
        choice = "3"
        nb_cards = 0
        compteur_fini = 0
        stop = 0
        for i in range(len(g.players)):
            print(g.players[i].name, ":", len(g.players[i].hand), "cartes")
            g.players[i].role = ""
            g.players[i].finish = 0

        while tour < len(g.players) - 1:
            if stop == 1:
                break
            for i in range(len(g.players)):
                if stop == 1:
                    break
                choix = ""
                if tour == len(g.players) - 1:
                    break
                if g.players[i].ordre == 0:
                    if len(g.players[i].hand) == 0:
                        g.players[i].finish = 1
                        compteur_president = 0
                        for p in range(len(g.players)):
                            if g.players[p].role == "Président":
                                compteur_president = 1
                        if compteur_president == 0:
                            g.players[i].role = "Président"
                    if i == 0:
                        if g.players[i].finish == 1:
                            pass
                        else:
                            print('Carte dans ta main : ')
                            print(g.main_player.hand, )
                            # deck = Label(text=g.main_player.hand, font=("Arial Bold", 15), fg='yellow', bg='black')
                            # deck.pack()
                            # # continu = tkinter.Button(text="Continuer", command=window.quit)
                            # # continu.pack()
                            # window.mainloop()
                            # tentative d'affichage du deck source de nombreux bug

                            #Le joueur choisi la carte qu'il veut jouer et on compare la carte avec la valeur du joueur precedent
                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                            while choix > choice:
                                if choix == "V" and (choice == "D" or choice == "R" or choice == "A"):
                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                elif choix == "D" and choice == "A":
                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                elif choix == "R" and choice == "A":
                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                elif choice == "10" and (
                                        choix == "3" or choix == "4" or choix == "5" or choix == "6" or choix == "7" or choix == "8" or choix == "9"):
                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                else:
                                    break
                            while choix < choice:
                                if choice == "V" and (choix == "D" or choix == "R" or choix == "A"):
                                    break
                                elif choice == "D" and (choix == "R" or choix == "A"):
                                    break
                                elif choice == "R" and choix == "A":
                                    break
                                elif choix == "10" and (choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9"):
                                    break
                                elif choix == "0" or choix == "2":
                                    break
                                choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                            while g.players[i].has_symbol(choix) < nb_cards:
                                if nb_cards == 0 or choix == "0":
                                    break
                                choix = input('Quel carte veux-tu jouer? (0 pour passer)')
                            if choix == "0":
                                plays = g.main_player.play([])
                                tour = tour + 1
                            else:
                                choice = choix
                                plays = g.main_player.play(choice)
                                tour = 0
                                last_player = "You"

                            print(f"Tu as joué {plays}")
                            if len(plays) == 0 and nb_cards == 0:
                                nb_cards = 1
                            elif len(plays) == 0 and nb_cards > 0:
                                nb_cards = nb_cards
                            else:
                                nb_cards = len(plays)
                    else:
                        if g.players[i].finish == 1:
                            pass
                        else:
                            if plays != [] and (choice == "2" or nb_cards == 4):
                                tour = len(g.players) - 1
                                last_player = "You"
                                break
                            plays = g.players[i].play(choice, nb_cards)
                            print(f"{g.players[i].name} joue \t {plays}")
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
                        if len(g.players[j].hand) == 0:
                            g.players[j].finish = 1
                        if g.players[j].ordre == 1:
                            if len(g.players[j].hand) == 0:
                                g.players[j].finish = 1
                                compteur_president = 0
                                for p in range(len(g.players)):
                                    if g.players[p].role == "Président":
                                        compteur_president = 1
                                if compteur_president == 0:
                                    g.players[j].role = "Président"
                            if j == 0:
                                if g.players[j].finish == 1:
                                    pass
                                else:
                                    print('Carte dans ta main : ')
                                    print(g.main_player.hand, )
                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                    while choix > choice:
                                        if choix == "V" and (choice == "D" or choice == "R" or choice == "A"):
                                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                        elif choix == "D" and choice == "A":
                                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                        elif choix == "R" and choice == "A":
                                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                        elif choice == "10" and (
                                                choix == "3" or choix == "4" or choix == "5" or choix == "6" or choix == "7" or choix == "8" or choix == "9"):
                                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                        else:
                                            break
                                    while choix < choice:
                                        if choice == "V" and (choix == "D" or choix == "R" or choix == "A"):
                                            break
                                        elif choice == "D" and (choix == "R" or choix == "A"):
                                            break
                                        elif choice == "R" and choix == "A":
                                            break
                                        elif choix == "10" and (
                                                choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9"):
                                            break
                                        elif choix == "0" or choix == "2":
                                            break
                                        choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                    while g.players[j].has_symbol(choix) < nb_cards:
                                        if nb_cards == 0 or choix == "0":
                                            break
                                        choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                    if choix == "0":
                                        plays = g.main_player.play([])
                                        tour = tour + 1
                                    else:
                                        choice = choix
                                        plays = g.main_player.play(choice)
                                        tour = 0
                                        last_player = "You"

                                    print(f"Tu as joué {plays}")
                                    if len(plays) == 0 and nb_cards == 0:
                                        nb_cards = 1
                                    elif len(plays) == 0 and nb_cards > 0:
                                        nb_cards = nb_cards
                                    else:
                                        nb_cards = len(plays)
                            else:
                                if g.players[j].finish == 1:
                                    pass
                                else:
                                    if plays != [] and (choice == "2" or nb_cards == 4):
                                        tour = len(g.players) - 1
                                        last_player = "You"
                                        break
                                    plays = g.players[j].play(choice, nb_cards)
                                    print(f"{g.players[j].name} joue \t {plays}")
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
                                if len(g.players[k].hand) == 0:
                                    g.players[k].finish = 1
                                if g.players[k].ordre == 2:
                                    if len(g.players[k].hand) == 0:
                                        g.players[k].finish = 1
                                        compteur_president = 0
                                        for p in range(len(g.players)):
                                            if g.players[p].role == "Président":
                                                compteur_president = 1
                                        if compteur_president == 0:
                                            g.players[k].role = "Président"
                                    if k == 0:
                                        if g.players[k].finish == 1:
                                            pass
                                        else:
                                            print('Carte dans ta main : ')
                                            print(g.main_player.hand, )
                                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                            while choix > choice:
                                                if choix == "V" and (choice == "D" or choice == "R" or choice == "A"):
                                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                                elif choix == "D" and choice == "A":
                                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                                elif choix == "R" and choice == "A":
                                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                                elif choice == "10" and (
                                                        choix == "3" or choix == "4" or choix == "5" or choix == "6" or choix == "7" or choix == "8" or choix == "9"):
                                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                                else:
                                                    break
                                            while choix < choice:
                                                if choice == "V" and (choix == "D" or choix == "R" or choix == "A"):
                                                    break
                                                elif choice == "D" and (choix == "R" or choix == "A"):
                                                    break
                                                elif choice == "R" and choix == "A":
                                                    break
                                                elif choix == "10" and (
                                                        choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9"):
                                                    break
                                                elif choix == "0" or choix == "2":
                                                    break
                                                choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                            while g.players[k].has_symbol(choix) < nb_cards:
                                                if nb_cards == 0 or choix == "0":
                                                    break
                                                choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                            if choix == "0":
                                                plays = g.main_player.play([])
                                                tour = tour + 1
                                            else:
                                                choice = choix
                                                plays = g.main_player.play(choice)
                                                tour = 0
                                                last_player = "You"

                                            print(f"Tu as joué {plays}")
                                            if len(plays) == 0 and nb_cards == 0:
                                                nb_cards = 1
                                            elif len(plays) == 0 and nb_cards > 0:
                                                nb_cards = nb_cards
                                            else:
                                                nb_cards = len(plays)
                                    else:
                                        if g.players[k].finish == 1:
                                            pass
                                        else:
                                            if plays != [] and (choice == "2" or nb_cards == 4):
                                                tour = len(g.players) - 1
                                                last_player = "You"
                                                break
                                            plays = g.players[k].play(choice, nb_cards)
                                            print(f"{g.players[k].name} joue \t {plays}")
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
                                        if len(g.players[l].hand) == 0:
                                            g.players[l].finish = 1
                                        if g.players[l].ordre == 3:
                                            if len(g.players[l].hand) == 0:
                                                g.players[l].finish = 1
                                                compteur_president = 0
                                                for p in range(len(g.players)):
                                                    if g.players[p].role == "Président":
                                                        compteur_president = 1
                                                if compteur_president == 0:
                                                    g.players[l].role = "Président"
                                            if l == 0:
                                                if g.players[l].finish == 1:
                                                    pass
                                                else:
                                                    print('Carte dans ta main : ')
                                                    print(g.main_player.hand, )
                                                    choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                                                    while choix > choice:
                                                        if choix == "V" and (
                                                                choice == "D" or choice == "R" or choice == "A"):
                                                            choix = input(
                                                                'Quel carte veux-tu jouer ? (0 pour passer)')
                                                        elif choix == "D" and choice == "A":
                                                            choix = input(
                                                                'Quel carte veux-tu jouer ? (0 pour passer)')
                                                        elif choix == "R" and choice == "A":
                                                            choix = input(
                                                                'Quel carte veux-tu jouer ? (0 pour passer)')
                                                        elif choice == "10" and (
                                                                choix == "3" or choix == "4" or choix == "5" or choix == "6" or choix == "7" or choix == "8" or choix == "9"):
                                                            choix = input(
                                                                'Quel carte veux-tu jouer ? (0 pour passer)')
                                                        else:
                                                            break
                                                    while choix < choice:
                                                        if choice == "V" and (
                                                                choix == "D" or choix == "R" or choix == "A"):
                                                            break
                                                        elif choice == "D" and (choix == "R" or choix == "A"):
                                                            break
                                                        elif choice == "R" and choix == "A":
                                                            break
                                                        elif choix == "10" and (
                                                                choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9"):
                                                            break
                                                        elif choix == "0" or choix == "2":
                                                            break
                                                        choix = input(
                                                            'Quel carte veux-tu jouer ? (0 pour passer')
                                                    while g.players[l].has_symbol(choix) < nb_cards:
                                                        if nb_cards == 0 or choix == "0":
                                                            break
                                                        choix = input(
                                                            'Quel carte veux-tu jouer ? (0 pour passer)')
                                                    if choix == "0":
                                                        plays = g.main_player.play([])
                                                        tour = tour + 1
                                                    else:
                                                        choice = choix
                                                        plays = g.main_player.play(choice)
                                                        tour = 0
                                                        last_player = "You"

                                                    print(f"Tu as joué {plays}")
                                                    if len(plays) == 0 and nb_cards == 0:
                                                        nb_cards = 1
                                                    elif len(plays) == 0 and nb_cards > 0:
                                                        nb_cards = nb_cards
                                                    else:
                                                        nb_cards = len(plays)
                                            else:
                                                if g.players[l].finish == 1:
                                                    pass
                                                else:
                                                    if plays != [] and (choice == "2" or nb_cards == 4):
                                                        tour = len(g.players) - 1
                                                        last_player = "You"
                                                        break
                                                    plays = g.players[l].play(choice, nb_cards)
                                                    print(f"{g.players[l].name} joue \t {plays}")
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
                compteur_fini = 0
                for i in range(len(g.players)):
                    if g.players[i].finish == 1:
                        compteur_fini = compteur_fini + 1
                    if compteur_fini == len(g.players) - 1:
                        for j in range(len(g.players)):
                            if g.players[j].finish == 0:
                                g.players[j].role = "Trouduc"
                                last_player = g.players[j].name
                            if g.players[j].role == "":
                                g.players[j].role = "Neutre"
                            if g.players[j].role == "Président":
                                g.players[j].score = g.players[j].score + 1
                            print(g.players[j].name, ":", g.players[j].role)
                        stop = 1
                        for i in range(len(g.players)):
                            g.players[i].start_hand
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
                        g.generate_cards()
                        g.distribute_cards()
                        g.nb_partie = g.nb_partie + 1
                        break

                if tour == len(g.players) - 1:
                    if last_player == "You":
                        print("Le tour est fini : Vous commencencez le tour")
                    else:
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


        wanna_continue = input('Est-ce que tu veux continuer (y/N)? ')
        wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')




if __name__ == '__main__':
    window = Tk()
    window.geometry("1680x1050")
    window.configure(bg='green')
    print_ln()
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    obj = tkinter.Label(text=""""           **********************************************
                   ** President : The cards game (TM) v.0.1 
                    L'interface graphique est encore en developpement 
                   ********************************************
                   Cliquez sur jouez pour lancez la partie
                   """, padx=500, anchor=CENTER, pady=100)
    obj.pack()
    bouton = tkinter.Button(text="Jouer", command=window.destroy)
    bouton.pack()
    liste = Label(text="Listes des joueurs de la partie :")
    liste.pack()
    g = PresidentGame()
    for i in range(len(g.players)):
        player_name = Label(text=g.players[i].name, font=("Arial Bold", 15), fg='yellow', bg='black')
        player_name.pack()
    window.mainloop()

    game_loop(g)
    partie = Label(text=f"Nombre de partie jouer :{g.nb_partie}")
    partie.pack()
    for i in range(len(g.players)):
        print(g.players[i].name, ":", g.players[i].score, "point(s)")
        scoring_name = Label(text=f"{g.players[i].name} victoire :")
        scoring = Label(text=g.players[i].score)
        scoring_name.pack()
        scoring.pack()
    print("Nombre de partie jouer :",g.nb_partie)
    print('Thank you for playing. I hope you enjoyed !')
    end = Label(text="Merci d'avoir joué. J'espère que tu as apprécié !", font=("Arial Bold", 15), fg='yellow',
                bg='black')
    end.pack()
    leave = tkinter.Button(text="Quitter", command=window.quit)
    leave.pack()
    window.mainloop()