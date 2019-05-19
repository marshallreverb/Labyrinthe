# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""
    
    def __init__(self, obstacles):
        self.grille = obstacles
        self.door = door(obstacles)
        
    
    def __cartify__(self,dic):  #fonction pour convertir le dictionnaire en carte 
        chaine  = ""
        for i,j in dic.keys():
            chaine = chaine + dic[i,j]
        return chaine
    
    
    def print_labyrinthe(self):
        chaine  = self.__cartify__(self.grille)  
        print(chaine)

    def lab_to_chaine(self):
       chaine  = self.__cartify__(self.grille)  
       return chaine

    def move (self,position,direction,step):
        #evluer la possibilité de mouvement sinon reste a la meme place 
        i=0
        while i<step:
            labyrinthe_card = addition_tuples(cardinals(direction),position)
            if labyrinthe_card in self.grille.keys() : 
                if self.grille[labyrinthe_card] != 'O' or self.grille[labyrinthe_card] != 'x': # si il existe un chemin 
                   self.grille[labyrinthe_card] = 'X'   #on deplace le robot vers la case vide 
                   self.grille[position] = ' '          #on supprime l'ancienne position du robot
                   position = labyrinthe_card
            i=i+1
    
    def add_X(self,position):
        if self.grille[position] == ' ':
            self.grille[position] = 'x'
            return True
        return False

    def murer(self,position):
        if self.grille[position] == ' ':
            self.grille[position]  = 'O'
            return True
        return False
    
    def percer(self,position):
        if self.grille[position] == 'O':
            self.grille[position]  = ' '
            return True
        return False


    def out(self,position):
        if position == self.door:
            return True
        return False

def door(dic): # return the door position 
    for i,valeur in dic.items():
        if valeur == 'U':
            
            return i

def cardinals(arg):
    mp = {
         'o':(1,0),
         "s":(0,1),
         "e":(-1,0),
         "n":(0,-1)
    }
    return mp.get(arg,(0,0))

#definition de la somme des tuples 
def addition_tuples(tuple1,tuple2):
    x,y = tuple2
    i,j = tuple1
    return (i+x,j+y)