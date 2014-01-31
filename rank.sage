load matrix_3c.py

def matrix_gf2_rank(matrix):
  n_rows = len(matrix)
  n_columns = len(matrix[0])
  MS = MatrixSpace(GF(2), n_rows, n_columns)
  matrix_gf2 = MS(matrix)
  return matrix_gf2.rank()

matrix = zip(*matrix_3c)
full_rank = matrix_gf2_rank(matrix)
print 'Rank of the full matrix: ' + repr(full_rank)

cells_to_move = []

# core, north pole
cells_to_move += [0]

# first layer, 10 cells. Changes 32 orbits
cells_to_move += [28, 35, 42, 46, 57, 66, 72, 94, 96, 98, 105, 109]

# second layer, 20 cells. Changes 24 orbits
cells_to_move += [8, 9, 13, 14, 16, 19, 21, 23, 25, 32, 43, 44, 58, 59, 69, 82, 91, 99, 103, 118]

# third layer, 12 cells. Changes 32 orbits
# cells_to_move += [27, 40, 49, 50, 54, 55, 80, 86, 89, 93, 104, 117]
# subset of third layer
cells_to_move += [27, 40, 49, 50, 54]

# fourth layer, equator, 30 cells. Changes 0 orbit
# cells_to_move += [1, 3, 4, 5, 6, 7, 24, 26, 30, 31, 34, 36, 37, 38, 39, 41, 53, 61, 63, 65, 70, 73, 76, 77, 78, 83, 88, 101, 102, 111]
# subset of equators
cells_to_move += [1, 3, 4, 24, 30, 34]

# south of equator
# cells_to_move += [29, 45, 47, 52, 68, 71, 84, 92, 100, 113, 114, 115]

# second layer south of equator
# cells_to_move += [10, 11, 12, 15, 17, 18, 20, 22, 33, 48, 51, 56, 60, 62, 87, 95, 108, 110, 112, 116]

# next to south pole
# cells_to_move += [64, 67, 74, 75, 79, 81, 85, 90, 97, 106, 107, 119]

# south pole
# cells_to_move += [2]

print 'Selecting ' + repr(len(cells_to_move)) + ' moves'
matrix_selected = [matrix[i] for i in cells_to_move]
selected_rank = matrix_gf2_rank(matrix_selected)

print 'Rank of the selected matrix: ' + repr(selected_rank)

if selected_rank == full_rank and len(cells_to_move) == full_rank:
  from cell120 import *
  cell120 = Cell120()
  for cell_index in cells_to_move:
    print cell_index, cell120.cells[cell_index].value
else:
  pass