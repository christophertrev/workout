import unittest
from baseMatrix import *


class TestBaseMatrix(unittest.TestCase):
  
  def setUp(self):
    self.testMatrix = baseMatrix(4)

  def testInstanciation(self):
    testMatrix  = baseMatrix(1,3)
    self.assertEqual(testMatrix.n ,1)
    self.assertEqual(testMatrix.m ,3)

  def testNoMInstance(self):
    testMatrix = baseMatrix(1)
    self.assertEqual(testMatrix.n ,1)
    self.assertEqual(testMatrix.m ,1)

  def testGetValueOfZeroFrom(self):
    self.assertEqual(self.testMatrix[0,1], 0)

  def testGetThrowOutOFBoundsError(self):
    with self.assertRaises(IndexError):
      self.testMatrix[-1,1]
    with self.assertRaises(IndexError):
      self.testMatrix[0,-1]
    with self.assertRaises(IndexError):
      self.testMatrix[10,1]
    with self.assertRaises(IndexError):
      self.testMatrix[1,10]

  def testReturnSetValue(self):
    testMatrix = baseMatrix(4)
    saveValue = 1 
    testMatrix[0,0] = saveValue
    self.assertEqual(testMatrix[0,0], saveValue)

  def testSetThrowOutOFBoundsError(self):
    with self.assertRaises(IndexError):
      self.testMatrix[-1,1] = 1
    with self.assertRaises(IndexError):
      self.testMatrix[0,-1] = 2
    with self.assertRaises(IndexError):
      self.testMatrix[10,1] = 2
    with self.assertRaises(IndexError):
      self.testMatrix[1,10] = 1

  def testAddMatrixReturnsNewMatrix(self):
    newMatrix = baseMatrix(1) + baseMatrix(1)
    self.assertIsInstance(newMatrix, baseMatrix)


  def testAddMatrixThrowErrorforMatrixOFUnEqualSize(self):
    with self.assertRaises(TypeError):
       baseMatrix(1) + baseMatrix(2)
     

if __name__ == '__main__':
  unittest.main()