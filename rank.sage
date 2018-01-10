load matrix_3c.py
load matrix_2c.py

def matrix_gf2_rank(matrix):
  n_rows = len(matrix)
  n_columns = len(matrix[0])
  MS = MatrixSpace(GF(2), n_rows, n_columns)
  matrix_gf2 = MS(matrix)
  return matrix_gf2.rank()

matrix_3c_skipped = matrix_3c[2:48]
# matrix_3c_skipped = matrix_3c[0:60]
print 'Selecting ' + repr(len(matrix_3c_skipped)) + ' orbits'
matrix = zip(*matrix_3c_skipped)

# matrix = zip(*matrix_3c)
full_rank = matrix_gf2_rank(matrix)
print 'Rank of the full matrix 3C: ' + repr(full_rank)

full_rank_2c = matrix_gf2_rank(matrix_2c)
print 'Rank of the full matrix 2C: ' + repr(full_rank_2c)

cells_to_move = []

# core, north pole
cells_to_move += [0]

# first layer, 10 cells. Changes 32 orbits
cells_to_move += [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# second layer, 20 cells. Changes 24 orbits
cells_to_move += [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

# third layer, 12 cells. Changes 32 orbits
cells_to_move += [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
# subset of third layer

# fourth layer, equator, 30 cells. Changes 0 orbit
cells_to_move += [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# subset of equators


# south of equator
# cells_to_move += [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]

# second layer south of equator
# cells_to_move += [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# next to south pole
# cells_to_move += [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]

# south pole
# cells_to_move += [119]

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