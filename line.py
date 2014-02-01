import unittest
import math
from vector import Vector

class Line:
  def __init__(self, v1, v2, moves = None):
    self.v1 = v1
    self.v2 = v2
    if moves == None:
      self.moves = set()
    else:
      self.moves = moves

  def add_moves(self, moves):
    self.moves = self.moves.union(moves)

  def center(self):
    return Vector(tuple([(a + b + 0.0) / 2 for a, b in zip(self.v1.value, self.v2.value)]))

  def direction(self):
    l = [a - b + 0.0 for a, b in zip(self.v1.value, self.v2.value)]
    if reduce(lambda x, y: 1e-7 * x + y, l) < 0:
      l = [-c for c in l]
    return Vector(tuple(l))

class LineTests(unittest.TestCase):
  def test_center(self):
    v1 = Vector((1, 0))
    v2 = Vector((0, 1))
    assert Line(v1, v2).center() == Vector((0.5, 0.5))

  def test_direction_1(self):
    v1 = Vector((1.5, 0))
    v2 = Vector((0, 2))
    assert Line(v1, v2).direction() == Line(v2, v1).direction()

  def test_direction_2(self):
    v1 = Vector((2, 0))
    v2 = Vector((0, 2))
    assert Line(v1, v2).direction() == Line(v2, v1).direction()

if __name__ == "__main__":
  unittest.main()
