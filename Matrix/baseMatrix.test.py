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

  def testEquality(self):
    self.assertEqual(baseMatrix(4),baseMatrix(4))

  def testEqaulityFails(self):
    newMatrix  = baseMatrix(4)
    newMatrix[0,0] = 1
    otherMat = baseMatrix(4)
    otherMat[0,0] = 22
    self.assertFalse(newMatrix == otherMat)

  def testMainIterator(self):
    predictedResults = [2,1,0,0]
    results = []
    mat = baseMatrix(2)
    mat[0,1] = 1
    mat[0,0] = 2
    for value in mat: 
      results.append(value)
    self.assertEqual(predictedResults, results)

  def testEqualityError(self):
    with self.assertRaises(TypeError):
      baseMatrix(3) == 2


  def testAddMatrixReturnsNewMatrix(self):
    newMatrix = baseMatrix(1) + baseMatrix(1)
    self.assertIsInstance(newMatrix, baseMatrix)


  def testAddMatrixThrowErrorforMatrixOFUnEqualSize(self):
    with self.assertRaises(TypeError):
       baseMatrix(1) + baseMatrix(2)

  def testAddReturnsCorrectMatrix(self):
    predictedResult = baseMatrix(2)
    predictedResult[0,0] = 1
    predictedResult[1,1] = 2 
    self.assertEqual(baseMatrix(2) + predictedResult, predictedResult)

if __name__ == '__main__':
  unittest.main()