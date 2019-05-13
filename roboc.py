# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            cartes.append(Carte(nom_carte,contenu))


# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

exist_game =False
# Si il y a une partie sauvegardée, on l'affiche, à compléter
for nom_fichier in os.listdir("save"):
    if nom_fichier.endswith(".s") :
        chemin = os.path.join("save", nom_fichier)
        print("reprise de la partie en cours ...")
        with open(chemin, "rb") as fichier:
            carte  = pickle.Unpickler(fichier).load()
            exist_game = True
            
if exist_game:
    reprise = input("une partie en cours a été trouvé voulez vous continuer(O/N) : ")
    if reprise.lower() == "n":
        choix = int(input("Entrez un numéro de labyrinthe pour commencer à jouer :")) 
        carte = cartes[choix-1]
else :
    choix = int(input("Entrez un numéro de labyrinthe pour commencer à jouer :")) 
    carte = cartes[choix-1]

win = 0
mouv = ""


try :
    while win == 0 and mouv != "q":#affichege du labyrinthe
        #on check si notre deplacment est winner

        carte.labyrinthe.print_labyrinthe()
        mouv = input()
        if mouv[0] in " s n o e":
            #si le mouv entré est correct on procède au deplacment du robot
            if len(mouv) == 1:
                step = 1
            else :
                if mouv[1].isdigit() : 
                    step = int(mouv[1]) 
            carte.labyrinthe.move(mouv[0],step)  
            
            #on enregistre le dernier mouvement
            
            chemin = os.path.join("save", "temp.s")
            with open(chemin, "wb") as fichier:
                    pickler  = pickle.Pickler(fichier)
                    pickler.dump(carte)
        if carte.labyrinthe.out():
            print("Félicitations ! Vous avez gagné !")
            os.remove(chemin) # *****
            win = 1
except KeyboardInterrupt:
    print("Arrêt de jeu (essayer (q) la prochaine fois ) ...")
        







