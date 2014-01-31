import random

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

# core, north pole
# cells_to_move += [0]

# first layer, 10 cells. Changes 32 orbits
# cells_to_move += [28, 35, 42, 46, 57, 66, 72, 94, 96, 98, 105, 109]

# second layer, 20 cells. Changes 24 orbits
# cells_to_move += [8, 9, 13, 14, 16, 19, 21, 23, 25, 32, 43, 44, 58, 59, 69, 82, 91, 99, 103, 118]

# third layer, 12 cells. Changes 32 orbits
# cells_to_move += [27, 40, 49, 50, 54, 55, 80, 86, 89, 93, 104, 117]

# fourth layer, equator, 30 cells. Changes 0 orbit
cells_to_move += [1, 3, 4, 5, 6, 7, 24, 26, 30, 31, 34, 36, 37, 38, 39, 41, 53, 61, 63, 65, 70, 73, 76, 77, 78, 83, 88, 101, 102, 111]

# south of equator
# cells_to_move += [29, 45, 47, 52, 68, 71, 84, 92, 100, 113, 114, 115]

# second layer south of equator
# cells_to_move += [10, 11, 12, 15, 17, 18, 20, 22, 33, 48, 51, 56, 60, 62, 87, 95, 108, 110, 112, 116]

# next to south pole
# cells_to_move += [64, 67, 74, 75, 79, 81, 85, 90, 97, 106, 107, 119]

# south pole
# cells_to_move += [2]

print repr(len(cells_to_move)) + ' cells flipped'

for cell_index in cells_to_move:
  initial_move[cell_index] = 1

gf2_moves = Move(initial_move)

scrambled_state = State3C(Matrix3C * gf2_moves)
print repr(list(scrambled_state).count(1)) + ' orbits changed'

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
