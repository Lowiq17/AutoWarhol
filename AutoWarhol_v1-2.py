

from turtle import *

from random import randint



######################################################################

###### Zone de définition des fonctions utiles #######################

######################################################################





def maison(cote):
    """ Doit dessiner une maison simple (carré + triangle par dessus)
    :param cote: longueur des côtés du carré et du triangle
    """
    seth(0)
    nbLignetoit=3
    nbLignecarre=4
    down()
    a=0
    b=0
    color('grey','grey')
    begin_fill()

    while b < nbLignecarre:
        b += 1
        forward(cote)
        left(360/nbLignecarre)
    end_fill()
    left(90)
    forward(cote)
    right(90)
    
    begin_fill()
    while a < nbLignetoit :
        color('red','red')
        
        a += 1
        forward(cote)
        left(360/nbLignetoit)
    end_fill()
    up()
    forward(cote)
    color("grey","grey")                    # Les 4 prochaines lignes servent a positioner et orienté correctement le crayon pour dessiner d'autre maison au même niveau 
    right(90)                        # Cela positionne donc le stylos en au coin en bas a droite de la maison 
    forward(cote)
    left(90)



def rue(nb_maisons):

    """ Doit dessiner une rue de maisons aléatoires, espacées aléatoirement dans la fenêtre
    :param nb_maisons: le nombre de maisons à dessiner à la suite
    """
    up()
    goto(-290,-285)
    a=0
    while a<nb_maisons :
        if nb_maisons > 5 :
            cote = randint(10,int(600/nb_maisons))    
        else :
            cote = randint(10,150)
        maison(cote)
        up()
        forward(cote/5)
        a+=1


def etoile(diametre, rotation,x,y):     # étoile à 5 branches

    """ Doit dessiner une étoile à 5 branches de diamètre donné, en partant avec un angle donné
    :param diamètre: diamètre de l'étoile (longueur des segments)
    :param rotation: angle de départ du crayon

    """

    seth(0)
    color("yellow")
    begin_fill()
    nbLignes=randint(5,10)
    if nbLignes % 2 == 0 :
        nbLignes +=1
    angle=360/nbLignes*2
    up()
    goto(x,y)
    
    left(rotation)
    down()
    a=0
    while a<nbLignes:
        a+=1
        forward(diametre)
        left(angle)
    end_fill()

def ciel_etoile(nb_etoiles):

    """ Doit produire un ciel étoilé au dessus de la maison en utilisant la fonction etoile
    :param nb_etoiles: nombre d'étoiles à dessiner
    """
    i=0
    while i < nb_etoiles:   
        diametre = randint(10,50)
        rotation = randint(0,360)
        x=randint(-250,250)
        y =randint(0,250)
        etoile(diametre, rotation,x,y)       
        i+=1
    
def comete() :   #Pas au point du tout ...
    i=0
    x=200
    y=200
    diametre = randint(10,30)
    pas = randint(5,10)
    nb_etoiles = randint (5,8)
    while i < nb_etoiles:   
        diametre = diametre - pas
        rotation = randint(0,90)
        x=x+pas
        y=y+pas
        etoile(diametre, rotation,x,y)       
        i+=1

        

############################################################################

##### Zone du programme qui dessine votre nuit étoilée #######

############################################################################



if __name__ == '__main__':

    nb_maisons = int(input("Combien de maisons voulez-vous ?  (<15)  "))            # <- ne pas modifier !!!
    nb_etoiles = int(input("Combien d'étoiles voulez-vous ?  "))                    # <- ne pas modifier !!!
    setup(600, 600)     # <- ne pas modifier !!!
    # Compléter le programme ici
    bgcolor("#0f056b")
    ht() 
    rue(nb_maisons)

    ciel_etoile(nb_etoiles)
    comete()   
    exitonclick()       # <- ne pas modifier !!!

