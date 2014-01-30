import unittest
import math
import itertools

class Vector:
  def __init__(self, value, norm = None):
    if norm == None:
      self.value = value
    else:
      self.value = tuple([c * 1.0 / norm for c in value])

  def __eq__(self, other):
    return isinstance(other, Vector) and (self.value == other.value or self.distance_to(other) < 1e-6)

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash(sum(int(c * 1e10) for c in self.value))

  def dimension(self):
    return len(self.value)

  def negate(self, index):
    l = list(self.value)
    l[index] = - l[index]
    return Vector(tuple(l))

  def plus_minus(self):
    pool = set([self])
    for index in range(self.dimension()):
      new_set = set([vector.negate(index) for vector in pool])
      pool = pool.union(new_set)
    return pool

  def even_perm(self):
    return self.perm_parity(0)

  def perm_parity(self, parity):
    l = list(self.value)
    if self.dimension() == 2:
      if parity == 0:
        return set([self])
      else:
        swap = Vector(tuple([l[1],l[0]]))
        return set([swap])

    pool = set()
    for index, value in enumerate(l):
      rest = Vector(tuple(l[:index] + l[(index + 1):]))
      rest_set = rest.perm_parity((index + parity) % 2)
      for rest_tuple in rest_set:
        pool.add(Vector(tuple([value] + list(rest_tuple.value))))
    return pool


  def plus_minus_all_perm(self):
    pool = self.plus_minus()
    new_pool = set()
    for vector in pool:
      for pv in itertools.permutations(vector.value):
        new_pool.add(Vector(pv))
    return new_pool

  def plus_minus_even_perm(self):
    pool = self.plus_minus()
    new_pool = set()
    for vector in pool:
      for pv in vector.even_perm():
        new_pool.add(pv)
    return new_pool

  def distance_to(self, vector):
    return sum((a - b) * (a - b) for a, b in zip(self.value, vector.value))

class VectorTests(unittest.TestCase):
  def test_eq(self):
    p = Vector((1, 2, 0, 0))
    q = Vector((1, 2, 0, 0))
    assert p == q

  def test_negate(self):
    p = Vector((1, 2, 0, 0))
    assert p.negate(1).value == (1, -2, 0, 0)

  def test_even_perm_2d(self):
    assert Vector((1,2)).even_perm() == set([Vector((1,2))])

  def test_even_perm_3d(self):
    assert Vector((1,2,3)).even_perm() == set([Vector((1,2,3)),Vector((3,1,2)),Vector((2,3,1))])

  def test_even_perm_4d(self):
    assert Vector((1,2,3,4)).even_perm() == set([
      Vector((1,2,3,4)),Vector((3,1,2,4)),Vector((2,3,1,4)), 
      Vector((2,1,4,3)),Vector((4,2,1,3)),Vector((1,4,2,3)), 
      Vector((1,3,4,2)),Vector((3,4,1,2)),Vector((4,1,3,2)),
      Vector((4,3,2,1)),Vector((3,2,4,1)),Vector((2,4,3,1))
    ])

  def test_plus_minus_2d(self):
    p = Vector((1, 2))
    assert p.plus_minus() == set([Vector((1, 2)), Vector((-1, 2)), Vector((-1, -2)), Vector((1, -2))])

  def test_plus_minus(self):
    p = Vector((1, 2, 0, 0))
    assert p.plus_minus() == set([
      Vector((1, 2, 0, 0)), 
      Vector((-1, 2, 0, 0)), 
      Vector((-1, -2, 0, 0)), 
      Vector((1, -2, 0, 0))
    ])

  def test_plus_minus_all_perm(self):
    p = Vector((1, 0))
    assert p.plus_minus_all_perm() == set([Vector((1, 0)), Vector((-1, 0)), Vector((0, 1)), Vector((0, -1))])

  def test_plus_minus_even_perm(self):
    p = Vector((1, 2, 0))
    assert p.plus_minus_even_perm() == set([
      Vector((1,2,0)),Vector((0,1,2)),Vector((2,0,1)),
      Vector((-1,2,0)),Vector((0,-1,2)),Vector((2,0,-1)),
      Vector((1,-2,0)),Vector((0,1,-2)),Vector((-2,0,1)),
      Vector((-1,-2,0)),Vector((0,-1,-2)),Vector((-2,0,-1))
    ])

  def test_distance_to_2d(self):
    p = Vector((1, 2))
    assert p.distance_to(Vector((2,3))) == 2

  def test_set(self):
    p = Vector((1, 2))
    q = Vector((1, 3))
    assert len(set([p, q])) == 2

  def test_set_close(self):
    p = Vector((1, 2))
    q = Vector((1, 2 + 1e-11))
    assert len(set([p, q])) == 1

if __name__ == "__main__":
  unittest.main()
