import tkinter
from models import PresidentGame, Affichage
from tkinter import *

def print_ln():
    print('\n')


def game_loop(g: PresidentGame):
    """
    The main game loop.
    Loops in circle until the user wants to quit the application.
    Args:
        g: The President Game instance.
    """
    #On initialise pour la première partie l'ordre dans le sens croissant et on ne met pas de role et un score à zéro
    for i in range(len(g.players)):
        g.players[i].ordre = i
        g.players[i].finish = 0
        g.players[i].role = ""
        g.players[i].score = 0
    #On met le nombre de partie à zéro et nous sommes le dernier joueur
    last_player = "You"
    g.nb_partie = 0

    wanna_continue = True
    while wanna_continue:
        #Boucle en fonction du nom de role (Président/Trouduc) et définie une variable pour récupérer le bon joueur et son role
        for i in range(len(g.players)):
            if g.players[i].role == "Président":
                president = g.players[i]
            if g.players[i].role == "Trouduc":
                trouduc = g.players[i]
        #Cette variable est réutiliser pour pouvoir donner une carte à la personne concerné
        for i in range(len(g.players)):
            if g.players[i].role == "Président":
                #Si nous sommes Président, nous pouvons choisir la carte à donner et donner au Trouduc
                if i == 0:
                    print(g.players[i].hand)
                    random_card = input("Donner une carte au Trouduc")
                    g.players[i].give_president(random_card, trouduc, g.main_player.hand)
                    g.players[i].remove_give_president(random_card, g.main_player.hand)
                #Sinon c'est la pire carte qui est prise à l'ordi et donner au Trouduc
                else:
                    random_card = g.players[i].hand[0]
                    g.players[i].give(random_card, trouduc)
                    g.players[i].remove_give(random_card)
            #Le Trouduc donne automatiquement sa meilleur carte au Président
            if g.players[i].role == "Trouduc":
                last_card = g.players[i].hand[-1]
                g.players[i].give(last_card, president)
                g.players[i].remove_give(last_card)

        #Le tour correspond au nombre de fois ou personne ne joue, on initilise le choice et nb_cards pour que l'ordi puissent jouer en premier
        tour = 0
        choice = "3"
        nb_cards = 0
        #Compte le nombre de joueur qui on fini de jouer
        compteur_fini = 0
        #Si stop est 1, on arrete le jeu, on le met donc à 0
        stop = 0
        #On dit le nombre de carte qu'a chaque joueur et on initialise les role et le nombre de personne qui on fini
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
                #Boucle de premier joueur
                if g.players[i].ordre == 0:
                    #Si plus de carte, on donne un role
                    if len(g.players[i].hand) == 0:
                        g.players[i].finish = 1
                        compteur_president = 0
                        #On vérifie s'il existe déja un Président, si oui il ne se passe rien sinon on donne le role Président
                        for p in range(len(g.players)):
                            if g.players[p].role == "Président":
                                compteur_president = 1
                        if compteur_president == 0:
                            g.players[i].role = "Président"
                    #Si c'est nous le joueur, on passe dans cette boucle
                    if i == 0:
                        # Si la personne à fini de joueur, on
                        if g.players[i].finish == 1:
                            pass
                        #Sinon on joue
                        else:
                            print('Carte dans ta main : ')
                            print(g.main_player.hand, )
                        # tentative d'affichage du deck source de nombreux bug avec tkinter
                            # deck = Label(text=g.main_player.hand, font=("Arial Bold", 15), fg='yellow', bg='black')
                            # deck.pack()
                            # # continu = tkinter.Button(text="Continuer", command=window.quit)
                            # # continu.pack()
                            # window.mainloop()

                            #Le joueur choisi la carte qu'il veut jouer et on compare la carte avec la valeur du joueur precedent
                            choix = input('Quel carte veux-tu jouer ? (0 pour passer)')
                            #Refaits des comparaison pour les lettres (la comparaison est par ordre alphabétique
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
                            #Nous empeche de jouer une carte plus petite que celui d'avant, mais execption pour les comparaison avec lettre, le 10, si nous ne jouons rien ou un 2
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
                            #Si nous jouons 1 carte alors que le joueur d'avant à jouer 2 cartes, on redemande de jouer (sauf si aucune carte)
                            while g.players[i].has_symbol(choix) < nb_cards:
                                if nb_cards == 0 or choix == "0":
                                    break
                                choix = input('Quel carte veux-tu jouer? (0 pour passer)')
                            #Si on écrit 0, le choice ne change pas et affiche comme ci nous ne jouons pas, le nombre de tour augmente
                            if choix == "0":
                                plays = g.main_player.play([])
                                tour = tour + 1
                            #Sinon, nous jouons notre carte et nous somme le dernier joueur, le nombre tour est rénitialiser
                            else:
                                choice = choix
                                plays = g.main_player.play(choice)
                                tour = 0
                                last_player = "You"

                            print(f"Tu as joué {plays}")
                            #Vérifie le nombre de carte jouer pour les suivants
                            if len(plays) == 0 and nb_cards == 0:
                                nb_cards = 1
                            elif len(plays) == 0 and nb_cards > 0:
                                nb_cards = nb_cards
                            else:
                                nb_cards = len(plays)
                    #Sinon c'est à l'ordi de jouer
                    else:
                        if g.players[i].finish == 1:
                            pass
                        else:
                            #Vérifie si nous n'avons pas jouer de 2 ou 4 cartes
                            if plays != [] and (choice == "2" or nb_cards == 4):
                                tour = len(g.players) - 1
                                last_player = "You"
                                break
                            plays = g.players[i].play(choice, nb_cards)
                            print(f"{g.players[i].name} joue \t {plays}")
                            #Vérifie si l'ordi n'a pas jouer de 2 ou 4 cartes
                            if plays != [] and (g.players[i].card_valeur == 15 or nb_cards == 4):
                                if len(plays) > 0:
                                    choice = plays[0].symbol
                                    last_player = g.players[i].name
                                    tour = len(g.players) - 1
                                break
                            #Si pas jouer : tour augment
                            if plays == []:
                                tour = tour + 1
                            #Sinon zéro et c'est le dernier joueur
                            if plays != []:
                                tour = 0
                                last_player = g.players[i].name
                            if len(plays) > 0:
                                choice = plays[0].symbol
                    #Même boucle mais pour le second joueur
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
                            #Même boucle mais pour le troisième joueur
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
                                    #Même boucle mais pour le quatrième joueur
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
                #Met le compteur de joueur fini à zéro
                compteur_fini = 0
                for i in range(len(g.players)):
                    #Si tel joueur à fini, le compteur augmente
                    if g.players[i].finish == 1:
                        compteur_fini = compteur_fini + 1
                    #Si le compteur est égale au nombre de joueur sauf 1, on fini la partie
                    if compteur_fini == len(g.players) - 1:
                        for j in range(len(g.players)):
                            #Celui qui n'a pas terminer est le Trouduc et est le premier joueur pour la prochaine partie
                            if g.players[j].finish == 0:
                                g.players[j].role = "Trouduc"
                                last_player = g.players[j].name
                            #Si il n'a pas de role il devient Neutre
                            if g.players[j].role == "":
                                g.players[j].role = "Neutre"
                            #Si président, son score augmente
                            if g.players[j].role == "Président":
                                g.players[j].score = g.players[j].score + 1
                            print(g.players[j].name, ":", g.players[j].role)
                        #Met le stop à 1 pour finir la partie (finir la boucle while initiale)
                        stop = 1
                        for i in range(len(g.players)):
                            #Enlève toute les cartes restante, surtout pour le Trouduc
                            g.players[i].start_hand
                            #Donne l'ordre de jeu pour la possible prochaine partie, le premier étant le Trouduc
                            if last_player == g.players[i].name:
                                #Correspond au joueur après le dernier joueur
                                after_last_player = i + 1
                                #Correspond au joueur qui se trouve a +2 du dernier joueur
                                after_after_last_player = i + 2
                                #Met l'ordre du dernier joueur à 0, premier joueur
                                g.players[i].ordre = 0
                                #Vérifie si le nombre est plus grand que le nombre de joueur pour lui définir à la main à qui cela correspond
                                if i + 1 > 3:
                                    after_last_player = 0
                                g.players[after_last_player].ordre = 1
                                if i + 2 == 4:
                                    after_after_last_player = 0
                                if i + 2 == 5:
                                    after_after_last_player = 1
                                g.players[after_after_last_player].ordre = 2
                                #Le joueur avant celui qui à gagner est le dernier
                                g.players[i - 1].ordre = 3
                        #Regenere un deck et les redistribue, le compteur de nombre de partie finie augmente
                        g.generate_cards()
                        g.distribute_cards()
                        g.nb_partie = g.nb_partie + 1
                        break

                if tour == len(g.players) - 1:
                    #Affiche le nom de dernier joueur lorsqu'un 2 est poser ou 4 cartes ou personne joue après une personne
                    if last_player == "You":
                        print("Le tour est fini : Vous commencencez le tour")
                    else:
                        print(f"Le tour est fini : {last_player} commence le tour")
                    #Donne l'ordre de jeu en partant du joueur qui à fini, même chose que lorque la partie est terminer
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

        #Demande si on veut rejouer
        wanna_continue = input('Est-ce que tu veux continuer (y/N)? ')
        wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')




if __name__ == '__main__':
    #Lance la fenetre graphique de présentation
    window = Tk()
    window.title("Le Président")
    window.geometry("1680x1050")
    window.configure(bg='green')
    print_ln()
    obj = tkinter.Label(text="""
**********************************************
Jeu de carte : Le Président par Axel et Jeanne
L'interface graphique est encore en développement 
**********************************************
                   
Cliquez sur jouer pour lancez la partie
                   """, font=("Arial Bold", 18), padx=150, anchor=CENTER, pady=50)
    obj.pack()
    liste = Label(text="Liste des joueurs de la partie :", font=("Arial Bold", 18), fg='white', bg='green', pady=10)
    liste.pack()
    g = PresidentGame()
    for i in range(len(g.players)):
        player_name = Label(text=g.players[i].name, font=("Arial Bold", 15), fg='white', bg='green', pady=5)
        player_name.pack()
    bouton = tkinter.Button(text="Jouer", command=window.destroy)
    bouton.pack()
    window.mainloop()

    #Lance le jeu dans le terminale
    game_loop(g)
    #Lorsqu'on ne relance pas de partie, lance l'interface graphique de fin
    window = Tk()
    window.title("Le Président")
    window.geometry("1680x1050")
    window.configure(bg='green')
    end = Label(text="Merci d'avoir joué. J'espère que tu as apprécié !", font=("Arial Bold", 20), fg='white',
                bg='green', pady=10)
    end.pack()
    #Affiche le nombre de partie jouer
    partie = Label(text=f"Nombre de partie jouer : {g.nb_partie}", font=("Arial Bold", 15), fg='white',
                bg='green', pady=10)
    partie.pack()
    #Affiche le score de chaque joueur : nombre de fois Président
    for i in range(len(g.players)):
        scoring_name = Label(text=f"{g.players[i].name} victoire : {g.players[i].score}", font=("Arial Bold", 15), fg='white',
                bg='green', pady=5)
        scoring_name.pack()
    leave = tkinter.Button(text="Quitter", command=window.quit)
    leave.pack()
    window.mainloop()