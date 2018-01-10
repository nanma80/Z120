load matrix_lights_out.py

def matrix_gf2_rank(matrix):
  n_rows = len(matrix)
  n_columns = len(matrix[0])
  MS = MatrixSpace(GF(2), n_rows, n_columns)
  matrix_gf2 = MS(matrix)
  return matrix_gf2.rank()

full_rank = matrix_gf2_rank(matrix_lights_out)
print 'Rank of the full matrix: ' + repr(full_rank)
