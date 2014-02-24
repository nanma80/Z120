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

starting_orbit = 22
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

for cell_index in range(1):
# for cell_index in [0]:
  # Starting from a random state
  # scramble_moves = Move([random.randint(0, 1) for b in range(120)])
  # scramble_state = sub_matrix * scramble_moves
  # solving_moves = sub_matrix.solve_right(scramble_state)
  # solution = scramble_moves + solving_moves

  # # Starting from a given state
  raw_state = [0] * num_orbits
  raw_state[cell_index] = 1
  # print raw_state
  state = StateSub3C(raw_state)
  solution = sub_matrix.solve_right(state)

  cells_to_flip = index_all(solution, 1)

  print sub_matrix_2 * solution

  print solution
  print 'Flipping cells:'
  print index_all(solution, 1)
  print repr(cell_index) + ': ' + repr(len(cells_to_flip)) + ' cells flipped'

# Steps to solve 3C:
# 1. Solve orbit 59. If odd parity, flip cell 45 or any cell from 45 ~ 74
# 2. Solve orbits 47 ~ 58. If any has odd parity, flip 5 cells to fix parity.
#    For orbit 50, flipping cells [13, 15, 17, 23, 24]. One only needs to move second layer cells
#    For orbit 55, flipping cells [13, 18, 22, 24, 25], a circle of second layer cells. 
#      The circle of cells flip 23 orbits:
#      [0, 2, 4, 5, 8, 10, 11, 12, 13, 17, 19, 20, 23, 25, 30, 31, 32, 36, 37, 42, 43, 44, 55]
# 3. Solve orbits 27 ~ 46. If any has odd parity, flip 9 cells to fix parity.
#    For orbit 27, flipping cells [7, 8, 12, 18, 19, 25, 26, 28, 31]. One only needs to move first and second layer cells.
#      A cluster of three first layer cells, around one dodecahedral vertex, and six second layer cells from six vertices on the three pentagons but not adjacent to the central vertex
#      7 orbits changed: [5, 6, 9, 20, 22, 25, 27]. One yellow strut, three long red struts, three blue struts
# 4. Solve orbits 15 ~ 26. Although 12 orbits need to be solved, the additional rank is only 5
#    Orbits 22 ~ 26 can be solved one by one, in descending order. After that, orbits 15 ~ 21 will be solved automatically
#    One needs to move the first four layers (including equator)
#    Orbit 22: [5, 9, 10, 12, 21, 23, 25, 27, 28, 29, 30, 32, 46, 47, 51, 53]
# 5 (0.5, -0.3090169943749474, 0, 0.8090169943749475)
# 9 (-0.5, 0.3090169943749474, 0, 0.8090169943749475)
# 10 (-0.3090169943749474, 0, 0.5, 0.8090169943749475)
# 12 (0.3090169943749474, 0, -0.5, 0.8090169943749475)
# 21 (-0.8090169943749475, 0, 0.3090169943749474, 0.5)
# 23 (0, 0.3090169943749474, 0.8090169943749475, 0.5)
# 25 (0.8090169943749475, 0, -0.3090169943749474, 0.5)
# 27 (0, 0.3090169943749474, -0.8090169943749475, 0.5)
# 28 (-0.3090169943749474, -0.8090169943749475, 0, 0.5)
# 29 (0.3090169943749474, 0.8090169943749475, 0, 0.5)
# 30 (0, -0.3090169943749474, 0.8090169943749475, 0.5)
# 32 (0, -0.3090169943749474, -0.8090169943749475, 0.5)
# 46 (0, -1, 0, 0)
# 47 (1, 0, 0, 0)
# 51 (-0.8090169943749475, 0.3090169943749474, 0.5, 0)
# 53 (0.3090169943749474, 0.5, -0.8090169943749475, 0)
#      10 orbits changed: [2, 3, 6, 7, 10, 13, 16, 17, 21, 22]
# 5. Solve orbits 0 ~ 14. Although 15 orbits need to be solved, the additional rank is only 6
#    Orbits 9 ~ 14 can be solved one by one, in descending order. After that, orbits 0 ~ 8 will be solved automatically
#    One needs to move the first three layers
#      Orbit 9: [0, 1, 2, 8, 10, 11, 12, 13, 14, 18, 19, 21, 24, 25, 30, 31, 32, 34, 35]
# 0 (0, 0, 0, 1)
# 1 (0.3090169943749474, 0, 0.5, 0.8090169943749475)
# 2 (0, 0.5, 0.3090169943749474, 0.8090169943749475)
# 8 (-0.3090169943749474, 0, -0.5, 0.8090169943749475)
# 10 (-0.3090169943749474, 0, 0.5, 0.8090169943749475)
# 11 (0, 0.5, -0.3090169943749474, 0.8090169943749475)
# 12 (0.3090169943749474, 0, -0.5, 0.8090169943749475)
# 13 (0.5, 0.5, 0.5, 0.5)
# 14 (-0.5, 0.5, 0.5, 0.5)
# 18 (0.5, 0.5, -0.5, 0.5)
# 19 (-0.5, 0.5, -0.5, 0.5)
# 21 (-0.8090169943749475, 0, 0.3090169943749474, 0.5)
# 24 (0.8090169943749475, 0, 0.3090169943749474, 0.5)
# 25 (0.8090169943749475, 0, -0.3090169943749474, 0.5)
# 30 (0, -0.3090169943749474, 0.8090169943749475, 0.5)
# 31 (-0.8090169943749475, 0, -0.3090169943749474, 0.5)
# 32 (0, -0.3090169943749474, -0.8090169943749475, 0.5)
# 34 (0, -0.8090169943749475, -0.5, 0.3090169943749474)
# 35 (0, -0.8090169943749475, 0.5, 0.3090169943749474)
#      1 center + 6 first layer + 10 second layer + 2 third layer
#      7 orbits changed: [2, 3, 5, 6, 7, 8, 9], all blue struts
# 6 (0.2700907567377264, 0.0, 0.0, 0.0)
# 3 (0.0, 0.2700907567377264, 0.0, 0.0)
# 8 (-0.0, -0.0, 0.2700907567377264, -0.0)
# 2 (-0.13504537836886324, 0.2185080122244105, 0.08346263385554728, -0.0)
# 7 (0.1350453783688632, 0.21850801222441052, 0.08346263385554728, 0.0)
# 5 (0.13504537836886324, -0.21850801222441052, 0.08346263385554731, -0.0)
# 9 (-0.13504537836886324, -0.2185080122244105, 0.08346263385554728, -0.0)

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
