
class baseMatrix():
  """docstring for baseMatrix
  creates matrixes that are n x m 
  """
  def __init__(self, n, m=None):
    if m is None: 
      m = n
    self.n = n
    self.m = m
    
