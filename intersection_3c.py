from matrix_2c import *
from matrix_3c import *

def histogram(matrix):
  intersection_histogram = {}
  row0 = matrix[0]
  for row in matrix:
    intersection = [a * b for a, b in zip(row0, row)].count(1)
    intersection_histogram[intersection] = intersection_histogram.get(intersection, 0) + 1
  return intersection_histogram

print 'Intersection between two orbits: '
print histogram(matrix_3c)
print
print 'Intersection between two cells: '
print histogram(zip(*matrix_3c))

