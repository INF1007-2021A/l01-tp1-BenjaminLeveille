import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):

    vitesseInitiale_Ms= vitesseInitiale/3.6
    vitesseFinale_Ms= vitesseFinale/3.6

    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    acceleration = (vitesseFinale_Ms - vitesseInitiale_Ms)/duree
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale =positionInitiale+vitesseInitiale_Ms*duree +acceleration/2*(duree**(2))

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
