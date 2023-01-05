from abc import ABC, abstractmethod
from math import pi, sqrt

class FormeGeometrique(ABC):

    @abstractmethod
    def perimetre(self):
        pass

    @abstractmethod
    def surface(self):
        pass

class Rectangle:
    """Permet de calculer le périmetre et la surface d'un rectangle"""
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._larguer = largeur
        self._nom = "rectangle"

    def perimetre(self):
        return f"Le périmètre du {self._nom} est: {2*(self._longueur + self._larguer)} mètre"

    def surface(self):
        return f"La surface du {self._nom} est: {self._longueur*self._larguer} mètre carré" 

class Cercle:
    """Permet de calculer le périmètre ou la circonférence et la surface du cercle"""
    def __init__(self, rayon):
        self._rayon = rayon

    def perimetre(self):
        return f"Le périmètre ou lacirconférence du cercle est: {2*pi*self._rayon} mètre "
    
    def surface(self):
        return f"La surface du cercle est: {pi*(self._rayon**2)} mètre carré"

class Triangle:
    """Permet de calculer le périmètre et la surface d'un triangle"""
    def __init__(self, cote_1, cote_2, cote_3):
        self._cote1 = cote_1
        self._cote2 = cote_2
        self._cote3 = cote_3
        self._nom = "triangle"

    def perimetre(self):
        return f"Le périmètre du {self._nom} est: {self._cote1 + self._cote2 + self._cote3} mètre "

    def surface(self):
        perimetre = self._cote1 + self._cote2 + self._cote3
        return f"""La surface du {self._nom} est: {sqrt((perimetre/2)*((perimetre/2) - self._cote1)
        *((perimetre/2) - self._cote2)*((perimetre/2) - self._cote3))} metrè carré"""

class Carre:
    """Permet de calculer le périmètre et la surface d'un Cercle"""
    def __init__(self, cote):
        self._longueur = cote
        self._larguer = cote
        self._nom = "carré"

    def perimetre(self):
        return f"Le périmètre du {self._nom} est: {self._longueur*4} mètre "

    def surface(self):
        return f"""La surface du {self._nom} est: {self._longueur*self._longueur} metrè carré"""

class TriangleRectangle:
    """Permet de calculer le périmètre et la surface d'un triangle rectangle"""
    def __init__(self, cote_1, cote_2):
        self._cote1 = cote_1
        self._cote2 = cote_2
        self._cote3 = sqrt((self._cote1**2) + (self._cote2**2))
        self._nom = "triangle réctangle"

    def perimetre(self):
        return f"Le périmètre du {self._nom} est: {self._cote1 + self._cote2 + self._cote3} mètre "

    def surface(self):
        perimetre = self._cote1 + self._cote2 + self._cote3
        return f"""La surface du {self._nom} est: {sqrt((perimetre/2)*((perimetre/2) - self._cote1)
        *((perimetre/2) - self._cote2)*((perimetre/2) - self._cote3))} metrè carré"""


def formeGemetrique(*figures):
    return [(figure.perimetre(), figure.surface()) for figure in figures]

