import unittest
from models.rectangle import Rectangle
"""
Module for unittests for the Rectangle class
"""


class TestRectangleClassCreation(unittest.TestCase):
    """Test class for Rectangle class instantiation tests"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height_only(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3)

    def test_height_width(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_inf_input(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, float('inf'), 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, float('inf'), 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, float('inf'), 6)

    def test_neg_inf_input(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-inf'), 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, float('-inf'), 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, float('-inf'), 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, float('-inf'), 6)

    def test_nan_input(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, float('nan'), 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, float('nan'), 6)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, float('nan'), 6)


    def test_width_height_x(self):
        r = Rectangle(3, 4, 5, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        self.assertIsNotNone(id)

    def test_check_int(self):
        with self.assertRaises(TypeError):
            r = Rectangle('f', 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 'f', 5, 6, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 'f', 6, 7)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 5, 'f', 7)

    def test_check_gr_0(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 5, 6, 7)
        with self.assertRaises(ValueError):
            r = Rectangle(2, -1, 5, 6, 7)

    def test_check_gr_eq_0(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, -1, 5, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 3, -5, 6)

    def test_area(self):
        r = Rectangle(3, 4, 3, 5, 6)
        self.assertEqual(r.area(), 12)

    

    # def test_id_negative(self):
    #     bo = Rectangle(-4)
    #     self.assertTrue(bo.id < 0)
    #     bo = Rectangle(-10)
    #     self.assertEqual(bo.id, -10)

    # def test_id_none(self):
    #     bo = Rectangle()
    #     self.assertEqual(bo.id, 1)
    #     bo = Rectangle(None)
    #     self.assertEqual(bo.id, 2)

    # def test_id_inf(self):
    #     bo = Rectangle(float('inf'))
    #     #TODO what should this do

    # def test_id_neg_inf(self):
    #     bo = Rectangle(float('-inf'))
    #     #TODO what should this do

    # def test_id_inf(self):
    #     bo = Rectangle(float('-inf'))
    #     #TODO what should this do

    # def test_id_inf(self):
    #     bo = Rectangle(float('NaN'))
    #     #TODO what should this do

    # def test_nb_objects(self):
    #     bo = Rectangle(23)
    #     self.assertEqual(Rectangle.__nb_objects, 0)
# def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())

  # def test_split(self):
  #     s = 'hello world'
  #     self.assertEqual(s.split(), ['hello', 'world'])
  #     # check that s.split fails when the separator is not a string
  #     with self.assertRaises(TypeError):
  #         s.split(2)

if __name__ == '__main__':
    unittest.main()
