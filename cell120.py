import unittest
import math
from vector import Vector
from line import Line
from orbit import Orbit

PHI = (math.sqrt(5) + 1)/2

class Cell120:
  def __init__(self):
    self.vertices = self.populate_vertices()
    self.cells = self.populate_cells()
    self.edges = self.populate_edges()
    self.faces = self.populate_faces()
    self.edge_orbits = self.populate_edge_orbits()
    self.face_orbits = self.populate_face_orbits()

  def populate_vertices(self):
    vertices = []
    norm = math.sqrt(8)
    vertices.extend(list(Vector((0, 0, 2, 2), norm).plus_minus_all_perm()))
    vertices.extend(list(Vector((1, 1, 1, math.sqrt(5)), norm).plus_minus_all_perm()))
    vertices.extend(list(Vector((1/PHI/PHI, PHI, PHI, PHI), norm).plus_minus_all_perm()))
    vertices.extend(list(Vector((1/PHI, 1/PHI, 1/PHI, PHI*PHI), norm).plus_minus_all_perm()))

    vertices.extend(list(Vector((0, 1/PHI/PHI, 1, PHI*PHI), norm).plus_minus_even_perm()))
    vertices.extend(list(Vector((0, 1/PHI, PHI, math.sqrt(5)), norm).plus_minus_even_perm()))
    vertices.extend(list(Vector((1/PHI, 1, PHI, 2), norm).plus_minus_even_perm()))
    return vertices

  def populate_cells(self):
    cells = []
    cells.extend(list(Vector((0.5, 0.5, 0.5, 0.5)).plus_minus()))
    cells.extend(list(Vector((0, 0, 0, 1)).plus_minus_all_perm()))
    cells.extend(list(Vector((PHI * 0.5, 0.5, 0, 0.5/PHI)).plus_minus_even_perm()))
    return cells

  def populate_edges(self):
    edges = []
    nv = len(self.vertices)
    for i in range(nv):
      for j in range(nv):
        if (i < j):
          distance = self.vertices[i].distance_to(self.vertices[j])
          if distance < 0.073:
            # found an edge
            edge = Line(self.vertices[i], self.vertices[j])
            moves = set()
            for k in range(len(self.cells)):
              cell = self.cells[k]
              if cell.distance_to(edge.center()) < 0.1306:
                moves.add(k)
            edge.add_moves(moves)
            edges.append(edge)
    return edges

  def populate_faces(self):
    faces = []
    nc = len(self.cells)
    for i in range(nc):
      for j in range(nc):
        if (i < j):
          distance = self.cells[i].distance_to(self.cells[j])
          if distance < 0.382:
            faces.append(Line(self.cells[i], self.cells[j], set([i, j])))
    return faces

  def populate_edge_orbits(self):
    orbits = {}
    for edge in self.edges:
      direction = edge.direction()
      if direction not in orbits:
        orbits[direction] = Orbit()
      orbits[direction].add_line(edge)
    return orbits.values()

  def populate_face_orbits(self):
    orbits = []
    faces = self.faces[:]

    for i in range(72):
      orbit = Orbit()
      face = faces[0]
      seed = faces.pop()
      orbit.add_line(seed)
      moves = list(seed.moves)
      axis = moves[0]
      for j in range(9):
        face_centers = [face.center() for face in faces]
        mirror_index = face_centers.index(seed.center().mirror_around(self.cells[axis]))
        seed = faces.pop(mirror_index)
        orbit.add_line(seed)
        moves = list(seed.moves)
        moves.remove(axis)
        axis = moves[0]

      orbits.append(orbit)

    return orbits

class Cell120Tests(unittest.TestCase):
  def test_basic_counts(self):
    c = Cell120()
    assert len(c.vertices) == 600
    assert len(c.cells) == 120
    assert len(c.edges) == 1200
    assert len(c.faces) == 720

  def test_edge_moves(self):
    c = Cell120()
    for edge in c.edges:
      assert len(edge.moves) == 3

  def test_face_moves(self):
    c = Cell120()
    for face in c.faces:
      assert len(face.moves) == 2

  def test_edge_orbits(self):
    c = Cell120()
    assert isinstance(c.edge_orbits, list)
    assert len(c.edge_orbits) == 60
    for orbit in c.edge_orbits:
      assert orbit.move_count() == 30
      assert orbit.line_count() == 20
    assert len(reduce(lambda x, y: x.union(y), [orbit.lines for orbit in c.edge_orbits])) == 1200

  def test_face_orbits(self):
    c = Cell120()
    assert isinstance(c.face_orbits, list)
    assert len(c.face_orbits) == 72
    for orbit in c.face_orbits:
      assert orbit.move_count() == 10
      assert orbit.line_count() == 10
    assert len(reduce(lambda x, y: x.union(y), [orbit.lines for orbit in c.face_orbits])) == 720

if __name__ == "__main__":
  unittest.main()

# 0.0729490168752: distance between adjacent vertices
# 0.38196601125: distance between adjacent cells
# 0.148770413178: distance from cell to adjacent vertices
# 0.130533158959: distance from cell to adjacent edge centers
