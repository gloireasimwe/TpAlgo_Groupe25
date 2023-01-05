from formGeometric import*
import time

debut = time.time()

# Test de la classe Rectangle
print('===Classe Rectangle===')
rectangle = Rectangle(7, 5)
print("Longueur =",rectangle._longueur, ";", "Largeur =", rectangle._larguer)
print("Périmètre: ",rectangle.perimetre(), "mètres")
print("Surface: ",rectangle.surface(),"mètres carrés", "\n")

# Test de la classe Cercle
print('===Classe Cercle===')
cercle = Cercle(5)
print("Rayon =", cercle._rayon)
print("Périmètre: ",cercle.perimetre(), "mètres")
print("Surface: ",cercle.surface(), "mètres carrés", "\n")

# Test de la classe Triangle
print('===Classe Triangle===')
triangle = Triangle(5, 6, 5)
print("Coté_1 =",triangle._cote1,";","Coté_2 =",triangle._cote2,";","Coté_3 =",triangle._cote3)
print("Périmètre: ",triangle.perimetre(), "mètres")
print("Surface: ",triangle.surface(), "mètres carrés", "\n")

# Test de la classe Carre
print('===Classe Carre===')
carre = Carre(4)
print("Coté =",carre._longueur)
print("Périmètre: ",carre.perimetre(), "mètres")
print("Surface: ",carre.surface(), "mètres carrés", "\n")

# Test de la classe TriangleRectangle
print('===Classe TriangleRectangle===')
triangleRectangle = TriangleRectangle(4,3)
print("Coté_1 =",triangleRectangle._cote1,";","Coté_2 =",triangleRectangle._cote2,";","Hypoténuse =",triangleRectangle._cote3)
print("Périmètre: ",triangleRectangle.perimetre(), "mètres")
print("Surface: ",triangleRectangle.surface(), "mètres carrés", "\n \n")

# Test de la classe PerimetreSurface
print("===Classe PerimetreSurface===")
perimetre = PerimetreSurface(rectangle, cercle, triangle, carre, triangleRectangle).get_perimetreSurface()
for i in perimetre:
    print("-->Figure: ", i[2],'\n',"Périmètre: ",i[0],"mètres", '\n',"Surface: ", i[1],"mètres carrés", '\n')

fin = time.time()

print("Temps d'éxcution: ", fin - debut)
