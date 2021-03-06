
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
    # Might want to add sorted array

  def __getitem__(self,key):
    self.checkInBounds(key)
    if key in self._storage:
      return self._storage[key]
    else: 
      return 0
    

  def __setitem__(self, key, value):
    self.checkInBounds(key)
    self._storage[key] = value

  def __add__ (self, other):
    self.checkEqualMatrixSize(self, other)
    result = baseMatrix(self.n, self.m)
    result._storage = self._storage
    for key in other._storage: 
      result[key[0], key[1]] += other._storage[key]
    return result

  def __eq__ (self,other):
    # might be able to just compare other._storage to self._storage
    if isinstance(other, baseMatrix):
      if(len(other._storage) != len(self._storage)):
        return False
      for key in self._storage:
        if key not in other._storage:
          return False
        if self._storage[key] != other._storage[key]:
          return False
      return True
        
    else: 
      raise TypeError

  def __float__(self):
    raise ValueError

  def __iter__(self):
    for row in xrange(0,self.n):
      for col in xrange(0,self.m):
        yield self[row,col]

  def __mul__(self, other):
    # print '__mul__'
    if self.isNumber(other):
      result = baseMatrix(self.n, self.m)
      for key in self._storage:
        result._storage[key] = self._storage[key]* other
      return result


    self.checkMultMatrixSize(self, other)
    newMatrix = baseMatrix(self.n, other.m)

    for key in self._storage:
      for col in xrange(0,other.m):
        if( other[key[1], col] != 0 ):
          newMatrix[key[0],col] += self._storage[key] * other[key[1],col]

    return newMatrix

  def isNumber(self, s):
      try:
          float(s)
          return True
      except ValueError:
          return False

  def checkInBounds(self, key):
    if key[0] < 0 or key[1] < 0:
      raise IndexError('index Out of bounds')
    if key[0] >= self.n or key[1] >= self.m:
      raise IndexError('index Out of bounds')



  def checkMultMatrixSize(self, leftMatrix, rightMatrix):
    if leftMatrix.m != rightMatrix.n:
      raise TypeError('"*" Matrix size does not equal.')


  def checkEqualMatrixSize(self,leftMatrix, rightMatrix):
    if leftMatrix.m != rightMatrix.m or leftMatrix.n != rightMatrix.n:
      raise TypeError('"+" Matrix size does not equal.')

if __name__ == '__main__':
  mat = baseMatrix(2)
  mat[0,1] = 1
  mat[0,0] = 2
  print mat._storage
  for key in mat._storage:
    print key 
  print mat.__class__.__name__
  for value in mat: 
    print value
