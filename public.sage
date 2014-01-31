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

original_moves = Move([random.randint(0, 1) for b in range(120)])

scrambled_state = State3C(Matrix3C * original_moves)
solution = Matrix3C.solve_right(scrambled_state)
all_moves_that_solve_3c = solution + original_moves

state_2c_when_3c_solved = Matrix2C * all_moves_that_solve_3c
print 'Starting from a random scramble, when 3C are solved, the state of 2C orbit is: (zero means even permutation)'
print state_2c_when_3c_solved

print ''
print 'The 2C matrix is:'
print Matrix2C

print 'The rank of the 2C matrix is: ' + str(Matrix2C.rank())

print ''
print 'The row space of the 2C matrix is: '
print Matrix2C.row_space()

print ''
print 'The 3C matrix is:'
print Matrix3C

print 'The rank of the 3C matrix is: ' + str(Matrix3C.rank())

print ''
print 'The row space of the 3C matrix is: '
print Matrix3C.row_space()

print ''
print 'The 2C + 3C matrix is:'
print Matrix2C3C

print 'The rank of the 2C + 3C matrix is: ' + str(Matrix2C3C.rank())
