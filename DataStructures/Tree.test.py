import unittest
from Tree import *


class TestBinaryTree(unittest.TestCase):
  
  def testAddChild(self):
    root = Node(5)
    root.addChild(10)
    self.assertTrue(root.rightChild.value, 10)
    root.addChild(1)
    self.assertTrue(root.leftChild.value, 1)

  def testContains(self):
    root = Node(5)
    root.addChild(10)
    root.addChild(1)
    self.assertTrue(root.contains(10))

  def testDepthFirstIter(self):
    results = []; 
    root = Node(5)
    root.addChild(10)
    root.addChild(1)
    root.addChild(4)
    root.addChild(2)
    root.addChild(8)
    root.addChild(12)
    for elem in root:
      results.append(elem)
    self.assertEqual(results, [1,2,4,5,8,10,12])    



if __name__ == '__main__':
  unittest.main()