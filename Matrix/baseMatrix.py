
class baseMatrix():
  """docstring for baseMatrix
  creates matrixes that are n x m 
  """
  def __init__(self, n, m=None):
    if m is None: 
      m = n
    self.n = n
    self.m = m
    self._storage = {}

  def __getitem__(self,key):
    self.checkInBounds(key)
    if key in self._storage:
      return self._storage[key]
    else: 
      return 0
    
  def __setitem__(self, key, value):
    self.checkInBounds(key)
    self._storage[key] = value


  def checkInBounds(self, key):
    if key[0] < 0 or key[1] < 0:
      raise IndexError('index Out of bounds')
    if key[0] >= self.n or key[1] >= self.m:
      raise IndexError('index Out of bounds')

  def __add__ (self, other):
    self.checkEqualMatrixSize(self, other)
    return baseMatrix(4)


  def checkEqualMatrixSize(self,leftMatrix, rightMatrix):
    if leftMatrix.m != rightMatrix.m or leftMatrix.n != rightMatrix.n:
      raise TypeError('"+" Matrix size does not equal.')

if __name__ == '__main__':
  mat = baseMatrix(2)
  mat[0,1] = 1
  mat[0,0] = 2
  print mat._storage
  print mat.__class__.__name__
