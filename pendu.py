
# ----------------- Jeu du pendu -----------------
import random as rd
import donnees

print("Bonjour et bienvenu dans le jeu du pendu.\n"
      "Un mot généré au hasard va vous être imposé.\n"
      "Vous aurez {} chances pour le trouver et pas une de plus!\n"
      "Si jamais vous échouez, la potence sera votre providence.\n"
      "Puisse le sort vous être favorable...\n".format(donnees.chances))

# Bloc permettant de choisir un mot au hasard dans "liste_mots" dans le fichier "donnees.py"

indice_mot = rd.randint(0, len(donnees.liste_mots) - 1)
word = donnees.liste_mots[indice_mot]  # Mot au hasard dans "liste_mots" à partir de son indice
print(word)

# Bloc permettant de décomposer notre mot en une liste de lettre
word_list = list(word)
print(word_list)

# Liste dans laquelle on va placer les lettres qu'on a trouvé
print("Le mot est composé de {} lettres, à vous de les trouver!".format(len(word)))
enigme = ["_" for i in range(len(word_list))]
# print(enigme)


while donnees.chances > 0 and enigme != word_list:

    print("".join(enigme))

    my_lettre = input("Entrez votre lettre:").lower()

    if my_lettre in word_list:  # Si notre lettre se trouve dans le mot à trouver alors:

        n = 0
        lettre_list = []  # On place notre lettre dans une liste

        for x in word_list:
            if x == my_lettre:
                ind = word.index(my_lettre, n, len(word))
                lettre_list += [ind]
                n = word.index(my_lettre) + 1

        for x in lettre_list:
            enigme[x] = my_lettre  # On place la lettre touvé

        # print(enigme)
        print("Vous avez trouvé la lettre '{}'.".format(my_lettre))

    else:
        print("Le mot ne contient pas la lettre \"{}\".".format(my_lettre))
        donnees.chances -= 1
        print("Il vous reste {} chances.".format(donnees.chances))

else:
    if enigme == word_list:
        print("Bravo! Vous avez réussi à trouver le mot: '{}'.".format(word))
    else:
        print("Vous êtes mort!!!")
        print("Le mot à trouver était \"{}\"".format(word))
        
