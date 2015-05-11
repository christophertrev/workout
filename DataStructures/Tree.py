# make a tree data stucture

class Node():
  """Treeeeee data structure. Left is less right is more"""
  def __init__(self, value):
    self.value = value
    self.leftChild = None
    self.rightChild = None

  def __iter__(self):
    if self.leftChild:
      for value in self.leftChild:
        yield value
    yield self.value
    if self.rightChild:
      for value in self.rightChild:
        yield value 

  def breadthFirst(self):
    yield self.value
    if self.leftChild: 
      yield self.leftChild.value
    if self.rightChild:
      yield self.rightChild.value

  def addChild(self, newValue):
    if(newValue == self.value):
      return 
    if newValue < self.value:
      # add on the left side
      if self.leftChild is None:
        self.leftChild = Node(newValue)
      else:
        self.leftChild.addChild(newValue)
    else: 
      if self.rightChild is None:
        self.rightChild = Node(newValue)
      else:
        self.rightChild.addChild(newValue)

  def contains(self, value):
    if value == self.value:
      return self
    elif value < self.value and self.leftChild:
      return self.leftChild.contains(value)
    elif value > self.value and self.rightChild:
      return self.rightChild.contains(value)
    else:
      return None



# Node(4).addChild(3).print()
# Node(4).rightChild()
# Node(4).rightChild/
root = Node(4)
root.addChild(5)
root.addChild(1)
root.addChild(2)
# print root.rightChild.value
# print root.leftChild.rightChild.value
for elem in root.breadthFirst():
  print elem
print root.contains(10)

