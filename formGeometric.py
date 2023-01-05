from abc import ABC, abstractmethod
from math import pi, sqrt

class FormeGeometrique(ABC):

    @abstractmethod
    def perimetre(self):
        pass

    @abstractmethod
    def surface(self):
        pass

class Rectangle(FormeGeometrique):
    """Permet de calculer le périmetre et la surface d'un rectangle"""
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._larguer = largeur
        self._nom = "Rectangle"

    def perimetre(self):
        return 2*(self._longueur + self._larguer)

    def surface(self):
        return self._longueur*self._larguer

class Cercle(FormeGeometrique):
    """Permet de calculer le périmètre ou la circonférence et la surface du cercle"""
    def __init__(self, rayon):
        self._rayon = rayon
        self._nom = "Cercle"

    def perimetre(self):
        return 2*(pi*self._rayon)
    
    def surface(self):
        return pi*(self._rayon**2)

class Triangle(FormeGeometrique):
    """Permet de calculer le périmètre et la surface d'un triangle"""
    def __init__(self, cote_1, cote_2, cote_3):
        self._cote1 = cote_1
        self._cote2 = cote_2
        self._cote3 = cote_3
        self._nom = "Triangle"

    def perimetre(self):
        return self._cote1 + self._cote2 + self._cote3

    def surface(self):
        perimetre = self._cote1 + self._cote2 + self._cote3
        return sqrt((perimetre/2)*((perimetre/2) - self._cote1)
        *((perimetre/2) - self._cote2)*((perimetre/2) - self._cote3))

class Carre(Rectangle):
    """Permet de calculer le périmètre et la surface d'un Cercle"""
    def __init__(self, cote):
        self._longueur = cote
        self._larguer = cote
        self._nom = "Carré"

class TriangleRectangle(Triangle):
    """Permet de calculer le périmètre et la surface d'un triangle rectangle"""
    def __init__(self, cote_1, cote_2):
        self._cote1 = cote_1
        self._cote2 = cote_2
        self._cote3 = sqrt((self._cote1**2) + (self._cote2**2))
        self._nom = "Triangle Réctangle"

class PerimetreSurface:
    """Permet de récupérer le périmètre et la surface d'une forme géométrique"""
    def __init__(self, *formeGeometrique:FormeGeometrique):
        self._formeGeo = formeGeometrique
    def get_perimetreSurface(self):
        return [(i.perimetre(),i.surface(), i._nom )for i in self._formeGeo]


    

