# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""
    
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = obstacles
        self._position = robot
        self.door = door(obstacles)
    
    def __cartify__(self,dic):  #fonction pour convertir le dictionnaire en carte 
        chaine  = ""
        for i,j in dic.keys():
            chaine = chaine + dic[i,j]
        return chaine
    
    def print_labyrinthe(self):
        chaine  = self.__cartify__(self.grille)  
        print(chaine)

    def move (self,direction,step):
        #evluer la possibilité de mouvement sinon reste a la meme place 
        position = self.robot 
        i=0
        while i<step:
            labyrinthe_card = addition_tuples(cardinals(direction),position)
            if labyrinthe_card in self.grille.keys() : 
                if self.grille[labyrinthe_card] == ' ' or self.grille[labyrinthe_card] == '.' or self.grille[labyrinthe_card] == 'U'  : # si il existe un chemin 
                   self.grille[labyrinthe_card] = 'X'   #on deplace le robot vers la case vide 
                   self.grille[position] = ' '          #on supprime l'ancienne position du robot
                   position = labyrinthe_card
            i=i+1
        self.robot = position
        #print(self.robot)

        
    def out(self):
        if self.robot == self.door:
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
    i,j = tuple1
    x,y = tuple2
    return (i+x,j+y)