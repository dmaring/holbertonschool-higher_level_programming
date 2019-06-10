import unittest
from models.base import Base
"""
Module for unittests for the Base class
"""


class TestBaseClassCreation(unittest.TestCase):
    """Test class for Base class instantiation tests"""

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

    def test_id_inf(self):
        bo = Base(float('inf'))
        #TODO what should this do

    def test_id_neg_inf(self):
        bo = Base(float('-inf'))
        #TODO what should this do

    def test_id_inf(self):
        bo = Base(float('-inf'))
        #TODO what should this do

    def test_id_inf(self):
        bo = Base(float('NaN'))
        #TODO what should this do

    # def test_nb_objects(self):
    #     bo = Base(23)
    #     self.assertEqual(Base.__nb_objects, 0)
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
