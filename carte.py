# -*-coding:Utf-8 -*

from labyrinthe import Labyrinthe

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)
        
        
    def __repr__(self):
        return "<Carte {}>".format(self.nom)
    
    def get_labyrinthe(self):
        return self.labyrinthe
        
def creer_labyrinthe_depuis_chaine(chaine):
       i=0
       j=1
       my_dic = dict()
       for lettre in chaine:  #on enrgistre chaque caractere et sa position dans un dic
           if lettre == '\n':
               j=j+1
               i=0
           my_dic[i,j] = lettre
           if lettre == 'X':
               robot = (i,j)    #pour l'instant on definira le robot par sa position sur la carte 
           i=i+1
       labyrinthe = Labyrinthe(robot,my_dic)
       return labyrinthe

