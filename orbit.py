import unittest
from vector import Vector
from line import Line

class Orbit:
  def __init__(self):
    self.lines = set()
    self.moves = set()

  def add_line(self, line):
    self.lines.add(line)
    self.moves = self.moves.union(line.moves)

  def line_count(self):
    return len(self.lines)

  def move_count(self):
    return len(self.moves)

class OrbitTests(unittest.TestCase):
  def test_initial_count(self):
    orbit = Orbit()
    assert orbit.line_count() == 0
    assert orbit.move_count() == 0

if __name__ == "__main__":
  unittest.main()
