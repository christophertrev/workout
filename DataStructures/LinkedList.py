class List():
  """docstring for Node"""
  def __init__(self, value):
    newNode = Node(value)
    self.start = newNode
    self.end = newNode

  def __iter__(self):
    current = self.start
    # yield current
    while current is not None:
      yield current 
      current = current.next

  def addToEnd(self, value):
    self.end.next = Node(value)
    self.end = self.end.next
    

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

 

root = List(4)
root.addToEnd(10)
root.addToEnd(14)
root.addToEnd(20)
# print root.end 
for node in root:
  print node.value
print root.start.value
print root.end.value
# root.addToEnd(4)
# print root.end
# for node in root:
#   print node 