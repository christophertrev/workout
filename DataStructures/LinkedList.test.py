import unittest
from LinkedList import *


class TestLinkedList(unittest.TestCase):
  
  def setUp(self):
    self.testList = List(4)
    # self.testList.addToEnd(10)

  def testStartValue(self):
    # testList = List(4)
    self.assertEqual(self.testList.start.value ,4)
    self.assertEqual(self.testList.end.value ,4)

  def testAddToEnd(self):
    self.testList.addToEnd(10)
    self.assertEqual(self.testList.start.value, 4)
    self.assertEqual(self.testList.end.value, 10)
    self.testList.addToEnd(30)  
    self.assertEqual(self.testList.end.value, 30)



if __name__ == '__main__':
  unittest.main()