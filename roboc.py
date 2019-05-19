# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
import os
import pickle
import socket
import select


from carte import Carte
from player import Player

HOST = ''
PORT = 7411
Server_lance = False
Client_lance = False

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def launch_server(HOST,PORT):
    try:
        connexion_principale.bind((HOST, PORT))
        connexion_principale.listen(5)
        print("Le serveur écoute à présent sur le port {}".format(PORT))
        return True
    except OSError:
        if OSError.strerror == "Address already in use":
            #launch_client()
            Server_lance = True
            return True
    
"""def launch_client():
    os.popen("python3 client.py")
    print("client lance")
    Client_lance = True
"""

Server_lance = launch_server (HOST,PORT)
    #launch_client()

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

choix = int(input("Entrez un numéro de labyrinthe pour commencer à jouer :")) 
carte = cartes[choix-1]

clients_connectes = []
players = []
while Server_lance :
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)
        #nouveau joueur 
        position = carte.add_player()
        players.append(Player(position,len(clients_connectes),connexion_avec_client))
        print("player added ")
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else :  
        for client in clients_a_lire : 
             msg_recu = client.recv(1024)
             msg_recu = msg_recu.decode()
             print("Recu {} ".format(msg_recu))
             client.send(b"yoyyo")
             if msg_recu == "fin":
                serveur_lance = False
            

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()

        
