import unittest
from baseMatrix import *


class TestBaseMatrix(unittest.TestCase):
  
  def setUp(self):
    # self.testMatrix = baseMatrix(1,3)
    pass

  def testInstanciation(self):
    testMatrix  = baseMatrix(1,3)
    self.assertEqual(testMatrix.n ,1)
    self.assertEqual(testMatrix.m ,3)

  def testNoMInstance(self):
    testMatrix = baseMatrix(1)
    self.assertEqual(testMatrix.n ,1)
    self.assertEqual(testMatrix.m ,1)





if __name__ == '__main__':
  unittest.main()