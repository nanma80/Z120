from cell120 import *

def orbits_to_matrix(orbits):
  matrix = []

  for orbit in orbits:
    row = []
    for i in range(120):
      if i in orbit.moves:
        row.append(1)
      else:
        row.append(0)
    matrix.append(row)

  return matrix

cell120 = Cell120()

with open('matrix_2c.py', 'w') as f:
  f.write('matrix_2c = ' + str(orbits_to_matrix(cell120.face_orbits)))
f.closed

with open('matrix_3c.py', 'w') as f:
  f.write('matrix_3c = ' + str(orbits_to_matrix(cell120.edge_orbits)))
f.closed
