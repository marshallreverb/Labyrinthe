# -*-coding:Utf-8 -*
from collections import OrderedDict
from labyrinthe import Labyrinthe

import random

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe,self.i,self.j = creer_labyrinthe_depuis_chaine(chaine)
    

        
    def __repr__(self):
        return "<Carte {}>".format(self.nom)
    
    def get_labyrinthe(self):
        return self.labyrinthe

    def add_player(self):
        position=generate_tuple(self.i,self.j)
        while not self.labyrinthe.add_X(position): #tant que la position n'est pas vide 
            position=generate_tuple(self.i,self.j)
        return position
    
    def carte_to_chaine(self):
        chaine= self.labyrinthe.lab_to_chaine()
        return chaine

def creer_labyrinthe_depuis_chaine(chaine):
       i=0
       j=0
       my_dic = OrderedDict()
       for lettre in chaine:  #on enrgistre chaque caractere et sa position dans un dic
           if lettre == '\n':
               j=j+1
               i=0
           my_dic[i,j] = lettre 
           i=i+1
       labyrinthe = Labyrinthe(my_dic)
       return labyrinthe,i,j

def generate_tuple(i,j):
    x = random.choice(range(0,i))
    y = random.choice(range(0,j))
    return (x,y)