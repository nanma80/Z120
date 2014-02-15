import random

def matrix_gf2(raw_matrix):
  n_rows = len(raw_matrix)
  n_columns = len(raw_matrix[0])
  MS = MatrixSpace(GF(2), n_rows, n_columns)
  matrix = MS(raw_matrix)
  return matrix

def index_all(enumerable, value):
  return [i for i, x in enumerate(enumerable) if x == value]

load matrix_2c.py
load matrix_3c.py

starting_orbit = 9
sub_matrix_3c = matrix_3c[starting_orbit:60]
num_orbits = len(sub_matrix_3c)
sub_matrix = matrix_gf2(sub_matrix_3c)
rank = rank(sub_matrix)
print num_orbits, rank, num_orbits - rank

sub_matrix_3c_2 = matrix_3c[0:starting_orbit]
sub_matrix_2 = matrix_gf2(sub_matrix_3c_2)

Move = VectorSpace(GF(2), 120)
State3C = VectorSpace(GF(2), 60)
StateSub3C = VectorSpace(GF(2), num_orbits)

# for cell_index in range(20):
for cell_index in [0]:
  # Starting from a random state
  scramble_moves = Move([random.randint(0, 1) for b in range(120)])
  scramble_state = sub_matrix * scramble_moves
  solving_moves = sub_matrix.solve_right(scramble_state)
  solution = scramble_moves + solving_moves

  # # Starting from a given state
  # raw_state = [0] * num_orbits
  # raw_state[cell_index] = 1
  # # print raw_state
  # state = StateSub3C(raw_state)
  # solution = sub_matrix.solve_right(state)

  cells_to_flip = index_all(solution, 1)

  print sub_matrix_2 * solution

  print solution
  print 'Flipping cells:'
  print index_all(solution, 1)
  print repr(cell_index) + ': ' + repr(len(cells_to_flip)) + ' cells flipped'

# Steps to solve 3C:
# 1. Solve orbit 59. If odd parity, flip cell 45 or any cell from 45 ~ 74
# 2. Solve orbits 47 ~ 58. If any has odd parity, flip 5 cells to fix parity.
#    For orbit 50, flipping cells [13, 15, 17, 23, 24]
# 3. Solve orbits 27 ~ 46. If any has odd parity, flip 9 cells to fix parity.
#    For orbit 27, flipping cells [7, 8, 12, 18, 19, 25, 26, 28, 31]
# 4. Solve orbits 15 ~ 26. Although 12 orbits need to be solved, the additional rank is only 5
#    Orbits 22 ~ 26 can be solved one by one, in descending order. After that, orbits 15 ~ 21 will be solved automatically
# 5. Solve orbits 0 ~ 14. Although 15 orbits need to be solved, the additional rank is only 6
#    Orbits 9 ~ 14 can be solved one by one, in descending order. After that, orbits 0 ~ 8 will be solved automatically



# Structure of orbits
# 0 ~ 14: 15 orbits pass the core: blue struts
# 15 ~ 26: 12 orbits pass the edges between second layer and third layer cells: long red struts
# 27 ~ 46: 20 orbits pass the extension of vertices from core, between the second layer cells: yellow struts
# 47 ~ 58: 12 orbits pass the edges between third layer and fourth layer cells: short red struts
# 59: 1 orbit orthogonal to the view. No strut


# Structure of the cells
# core, north pole
# cells_to_move += [0]

# first layer, 10 cells. Changes 32 orbits
# cells_to_move += [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# second layer, 20 cells. Changes 24 orbits
# cells_to_move += [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

# third layer, 12 cells. Changes 32 orbits
# cells_to_move += [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
# subset of third layer

# fourth layer, equator, 30 cells. Changes 0 orbit
# cells_to_move += [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# subset of equators

# south of equator
# cells_to_move += [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]

# second layer south of equator
# cells_to_move += [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# next to south pole
# cells_to_move += [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]

# south pole
# cells_to_move += [119]
