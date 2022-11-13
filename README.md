# Python Exercice : Le jeu du président

## Projet de cours en deuxième année 
Le président (aussi appelé le troufion) est un jeu de cartes rapide et amusant, au cours duquel la hiérarchie des joueurs changera à chaque manche.<br>
Le vainqueur d'une manche devient le président, alors que le perdant est proclamé trouduc (ou troufion).

## Nécessaire avant de lancer le jeu:
* Récupérer le projet :<br><br>
```git clone https://github.com/Jeannegbl/python-cardsgame-president.git ```<br><br>
* Installer le Nécéssaire :<br><br>
```pip install -r requirements.txt```<br><br>
* Pour avoir l'interface graphique :<br><br>
```sudo apt-get install python3-tk```

## Comment jouer:
Lancer la partie depuis la main en faisant un ```Run 'main'``` ce qui lance l'interface graphique affiche les joueurs présents dans la partie.
<br><br>
Pour le moment pas de possibilité de jouer avec l'interface graphique, il faut cliquer sur jouer pour continuer avec la console.<br>
Pour jouer une carte, il faut indiquer soit la valeur en chiffre pour les cartes numériques, soit le symbole pour V (Valet), D (Dame), R (Roi), A (As).
<br>
Pour passer son tour, que ce soit parce que vous ne pouvez pas ou vous ne voulez pas jouer mettez 0.<br><br>
À la fin de chaque parti, c'est-à-dire quand tout le monde sauf un joueur à utiliser toutes ces cartes, on propose de relancer une autre partie avec l'attribution des rôles suite à la partie d'avant.<br>

* ### Trouduc :
Le Trouduc donne automatiquement sa meilleure carte au président.
* ### Président :
Si vous êtes Président alors vous pouvez choisir la carte à donner au Trouduc.<br>
Sinon, l'ordi donne sa plus faible carte au Trouduc.<br>

Si vous ne relancez pas une autre partie l'interface graphique afficher le score final qui correspond aux nombres de fois que chaque joueur a été Président.<br>
Appuyez sur quitter pour terminer le programme.
