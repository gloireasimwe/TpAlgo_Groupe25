from formGeometric import*

import unittest

class Testing(unittest.TestCase):
    
    # ===========Rectangle============
    def test_perimetre_rectangle(self):
        a = Rectangle(8,5).perimetre()
        b = 26
        self.assertEqual(a,b)

    def test_surface_rectangle(self):
        a = Rectangle(8,5).surface()
        b = 40
        self.assertEqual(a,b)

    # ===========Cercle============
    def test_perimetre_cercle(self):
        a = Cercle(8).perimetre()
        b = 8*2*pi
        self.assertEqual(a,b)

    def test_surface_cercle(self):
        a = Cercle(8).surface()
        b = (8**2)*pi
        self.assertEqual(a,b)

    # ==========Triangle=============
    def test_perimetre_triangle(self):
        a = Triangle(4,3,5).perimetre()
        b = 12
        self.assertEqual(a,b)
    
    def test_surface_triangle(self):
        a = Triangle(4,3,5).surface()
        b = 6
        self.assertEqual(a,b)

    # ===========Carre============
    def test_perimetre_carre(self):
        a = Carre(8).perimetre()
        b = 32
        self.assertEqual(a,b)

    def test_surface_carre(self):
        a = Carre(8).surface()
        b = 64
        self.assertEqual(a,b)

    # ==========TriangleRectangle=============
    def test_perimetre_triangleRectangle(self):
        a = TriangleRectangle(4,3).perimetre()
        b = 12
        self.assertEqual(a,b)
    
    def test_surface_triangleRectangle(self):
        a = TriangleRectangle(4,3).surface()
        b = 6
        self.assertEqual(a,b)
    
if __name__ == '__main__':
    unittest.main()