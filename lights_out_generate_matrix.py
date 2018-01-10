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
matrix = []

for c1 in cell120.cells:
  row = []
  for c2 in cell120.cells:
    inner_product = 0.0
    for index in xrange(4):
      inner_product += c1.value[index] * c2.value[index]
    orthogonal = 0
    if inner_product < 1E-10 and inner_product > -1E-10:
      orthogonal = 1
    row.append(orthogonal)
  matrix.append(row)

print matrix

with open('matrix_lights_out.py', 'w') as f:
  f.write('matrix_lights_out = ' + str(matrix))
f.closed
