import random

def index_all(enumerable, value):
  return [i for i, x in enumerate(enumerable) if x == value]

load matrix_2c.py
load matrix_3c.py

MS2C = MatrixSpace(GF(2), 72, 120)
Matrix2C = MS2C(matrix_2c)

MS3C = MatrixSpace(GF(2), 60, 120)
Matrix3C = MS3C(matrix_3c)

MS2C3C = MatrixSpace(GF(2), 132, 120)
Matrix2C3C = MS2C3C(matrix_2c + matrix_3c)

Move = VectorSpace(GF(2), 120)
State2C = VectorSpace(GF(2), 72)
State3C = VectorSpace(GF(2), 60)

initial_move = [0] * 120

cells_to_move = []

# adhoc subset
# cells_to_move += [13, 18, 22, 24, 25]
# cells_to_move += [7, 8, 12, 18, 19, 25, 26, 28, 31]
# cells_to_move += [0, 1, 2, 8, 10, 11, 12, 13, 14, 18, 19, 21, 24, 25, 30, 31, 32, 34, 35]
cells_to_move += [5, 9, 10, 12, 21, 23, 25, 27, 28, 29, 30, 32, 46, 47, 51, 53]

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

print repr(len(cells_to_move)) + ' cells flipped'

for cell_index in cells_to_move:
  initial_move[cell_index] = 1

gf2_moves = Move(initial_move)

scrambled_state = State3C(Matrix3C * gf2_moves)
cells_flipped = index_all(scrambled_state, 1)

print repr(list(scrambled_state).count(1)) + ' orbits changed'
print cells_flipped

# for i in range(120):
#   if i > 0:
#     moves = initial_move[:]
#     moves[i] = 1

#     gf2_moves = Move(moves)

#     scrambled_state = State3C(Matrix3C * gf2_moves)
#     print list(scrambled_state).count(1)


# state_builder = [0] * 60
# state_builder[0] = 1

# for i in range(60):
#   state_builder2 = state_builder[:]
#   state_builder2[i] = 1

#   scrambled_state = State3C(state_builder2)
#   try:
#     solution = Matrix3C.solve_right(scrambled_state)
#     print str(i) + ': ' + str(solution)
#     print list(solution).count(1)
#   except ValueError:
#     pass
