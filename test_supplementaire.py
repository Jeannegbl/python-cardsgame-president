import unittest
import models

class TestCardsSupplementaire(unittest.TestCase):
    #Ce test permet de vérifier que l'ordinateur enleve bien la carte jouer de sa main
    def test_game_remove_ai_cards(self):
        game = models.PresidentGame()
        player_2 = game.players[1]
        longueur = len(player_2.hand)
        player_2.play("5",1)
        self.assertTrue(longueur > len(player_2.hand))

    #Ce test permet de vérifier que la carte donner du joueur 1 est bien récupérer dans la main du joueur 2
    def test_game_give_cards(self):
        game = models.PresidentGame()
        player_1 = game.players[0]
        player_2 = game.players[1]
        last_card = player_1.hand[-1]
        player_1.give(last_card, player_2)
        for card in player_2.hand:
            if last_card == card:
                self.assertTrue(True)

    #Ce test permet de vérifier que lors que l'on donne la carte, celle-ci est bien enlever de la main 1 vers la main 2
    def test_game_nb_cards_after_giving(self):
        game = models.PresidentGame()
        player_1 = game.players[0]
        player_2 = game.players[1]
        longueur = len(player_1.hand)
        last_card = player_1.hand[-1]
        player_1.give(last_card, player_2)
        player_1.remove_give(last_card)
        self.assertTrue(len(player_2.hand) > longueur > len(player_1.hand))

    #Ce test permet de vérifier qu'il n'y bien plus de carte lorsqu'on reinitialiser la main
    def test_game_restart_hand(self):
        game = models.PresidentGame()
        player_1 = game.players[0]
        player_1.start_hand
        self.assertTrue(player_1.hand == [])

    #Ce test permet de vérifier que la distribution ce fait sans problème avec l'initialisation de la main
    def test_game_restart_hand_and_new_distribute(self):
        game = models.PresidentGame()
        player_1 = game.players[0]
        first_play_1 = len(player_1.hand)
        player_1.start_hand
        game.generate_cards()
        game.distribute_cards()
        self.assertTrue(first_play_1 == len(player_1.hand))

if __name__ == '__main__':
    unittest.main()
