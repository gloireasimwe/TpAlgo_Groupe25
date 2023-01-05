from polymorphisme import*
import time

debut = time.time()

# Test de la classe Rectangle
rectangle = Rectangle(7, 5)
print(rectangle.perimetre())
print(rectangle.surface(), "\n")

# Test de la classe Cercle
cercle = Cercle(5)
print(cercle.perimetre())
print(cercle.surface(), "\n")

# Test de la classe Triangle
triangle = Triangle(5, 6, 5)
print(triangle.perimetre())
print(triangle.surface(), "\n")

# Test de la classe Carre
carre = Carre(4)
print(carre.perimetre())
print(carre.surface(), "\n")

# Test de la classe TriangleRectangle
triangleRectangle = TriangleRectangle(2,3)
print(triangleRectangle.perimetre())
print(triangleRectangle.surface(), "\n")

# Test de la fonction formeGeometrique
forme = formeGemetrique(rectangle, triangle, cercle, carre, triangleRectangle)
for i in forme:
    print(i[0], "||",i[1])

fin = time.time()

print("Temps d'éxcution: ", fin - debut)