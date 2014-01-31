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
initial_move[0] = 1

for i in range(120):
  if i > 0:
    moves = initial_move[:]
    # moves[i] = 1

    gf2_moves = Move(moves)

    scrambled_state = State3C(Matrix3C * gf2_moves)
    print list(scrambled_state).count(1)
