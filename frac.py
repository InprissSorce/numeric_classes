# Helpter functions

def approx_eq(f1, f2):
  return abs(f1 - f2) < 0.0000001

def reduce(a, b):
  '''
  Parameters: integers a and b that represent the fraction a/b
  Output: a tuple of integers that represent a/b fully reduced
  The Euclidean Algorithm is used.
  '''
  if a == b:
    return (1, 1)
  elif a < b:
    p = a
    q = b
  else:
    p = b
    q = a
  while (q % p) != 0:
    q, p = p, q % p
  return (a // p, b // p)

def findLCD(a, b):
  '''
  Parameters: integers a and b that represent the denominators of two fractions
  Output: integer p that represents the least common denominator of those two fractions
  Algorithm: If a less than b, increase a by a. If b less than a, increase b by b.
  Repeat. Continue until equal.
  '''
  p = a
  q = b
  while p != q:
    if p < q:
      p = p + a
    else:
      q = q + b
  return p


class frac:
  
  def __init__(self, n, d = 1):
    # Both n and d (if given) must be of type int.
    if not isinstance(n, int) or not isinstance(d, int):
      raise TypeError
    # No zero denominator.
    if d == 0:
      raise ValueError
    if n == 0:
      self.numerator = 0
      self.denominator = 1  
    else: 
      # Fractions begin life reduced.
      (reduced_numer, reduced_denom) = reduce(abs(n), abs(d))
      # If numer and denom have opposite signs, make numer negative.
      if n * d < 0:
        reduced_numer = -1 * reduced_numer
      else:
        reduced_numer, reduced_denom = abs(reduced_numer), abs(reduced_denom)
      self.numerator = reduced_numer
      self.denominator = reduced_denom

  def recip(self):
    return frac(self.denominator, self.numerator)
  
  def __eq__(self, second):
    if isinstance(second, float):
      return approx_eq(float(self), second)
    elif isinstance(second, int):
      second = frac(second) 
    return self.numerator * second.denominator == self.denominator * second.numerator

  def __ne__(self, second):
    return not self == second

  def __lt__(self, second):
    if isinstance(second, float):
      return float(self) < second
    elif isinstance(second, int):
      second = frac(second) 
    return self.numerator * second.denominator < self.denominator * second.numerator

  def __gt__(self, second):
    return not (self < second or self == second)

  def __le__(self, second):
    return self < second or self == second

  def __ge__(self, second):
    return self > second or self == second

  def __neg__(self):
    return frac(-self.numerator, self.denominator)

  def __abs__(self):
    return frac(abs(self.numerator), abs(self.denominator))

  def __add__(self, second):
    if isinstance(second, float):
      return float(self) + second    
    elif isinstance(second, int):
      second = frac(second, 1)
    lcd = findLCD(self.denominator, second.denominator)
    firstNumer = (lcd // self.denominator) * self.numerator
    secondNumer = (lcd // second.denominator) * second.numerator
    return frac(firstNumer + secondNumer, lcd)
  
  def __radd__(self, first):
    # self is the frac on the right
    # first is the non-frac on the left
    return self + first

  def __sub__(self, second):
    return self + -second
    
  def __rsub__(self, first):
    # self is the frac on the right
    # first is the non-frac on the left
    return -(self - first)

  def __mul__(self, second):
    if isinstance(second, float):
      return float(self) * second
    elif isinstance(second, int):
      second = frac(second)
    return frac(self.numerator * second.numerator, self.denominator * second.denominator)
  
  def __rmul__(self, first):
    # self is the frac on the right
    # first is the non-frac on the left
    return self * first
    
  def __truediv__(self, second):
    if isinstance(second, float):
      return float(self) / second
    elif isinstance(second, int):
      second = frac(second)
    return self * second.recip() 
  
  def __rtruediv__(self, first):
    # self is the frac on the right
    # first is the non-frac on the left
    if isinstance(first, float):
      return first / float(self)
    else:
      return (self / first).recip()

  def __pow__(self, power):
    if not isinstance(power, int):
      raise TypeError
    elif power >= 0:
      return frac(self.numerator ** power, self.denominator ** power)
    else:
      return frac(self.denominator ** abs(power), self.numerator ** abs(power))
  
  def __float__(self):
    return self.numerator / self.denominator

  def __int__(self):
    return int(float(self))
  
  def __repr__(self):
    return str(self.numerator) + '/' + str(self.denominator)
    