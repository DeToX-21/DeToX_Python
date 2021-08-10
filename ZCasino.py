""" Ce programme simule un jeu simplifé de la roulette."""

# Règle du jeu
# On choisit un numéro entre 0 et 49
# On place une mise
# Si numéro gagnant --> On gagne 3 fois la mise
# Si notre numéro et numéro gagnant paire ou impaire --> On récupère 50% de la mise
# Sinon on ne gagne rien
# Bonus: On peut jouer tant qu'il y'a de l'argent dans notre porte-monnaie (wallet).

from random import randrange
from math import ceil

wallet = 1000  # L'argent

while wallet > 0:

    number = int(input("Entrez un numéro entre 0 et 49:"))

    # Bloc permettant d'éviter de saisir un numéro non valide.
    while number < 0 or number >= 50:
        print("Votre numéro n'est pas compris entre 0 et 49.")
        number = int(input("Entrez un numéro entre 0 et 49:"))

    bet = int(input("Entrez le montant de votre mise:"))

    # Le joueur ne peut pas miser une somme supérieur à celle contenue dans le porte monnaie.
    while bet < 0 or bet > wallet:
        print("Vous devez entrer une mise inférieur à {}$!".format(wallet))
        bet = int(input("Entrez le montant de votre mise:"))

    wallet -= bet  # On retire la mise du porte monnaie.

    winning_number = randrange(50)  # Le numéro gagnant est générer au hasard.
    print("Le numéro gagnant est le {}!".format(winning_number))

    # Condition pour gagner ou non de l'argent.
    if number == winning_number:
        price = 3 * bet
        wallet += price
        print("Vous venez de gagner {}$!".format(price))
    elif number % 2 == winning_number % 2 == 0 or (number % 2 and winning_number % 2) != 0:
        price = ceil(0.5 * bet)
        wallet += price
        print("Vous récupérez {}$.".format(price))
    else:
        print("Vous avez perdu!!!")

    print("Il vous reste {}$ dans votre porte monnaie.".format(wallet))
else:
    print("Vous êtes fauché. GAME OVER !!!")
    quit()  # Losrque le porte monnaie est vide, on quitte le jeu.
