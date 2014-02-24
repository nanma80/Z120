from cell120 import *

cell120 = Cell120()

# for i in range(len(cell120.edge_orbits)):
#   orbit = cell120.edge_orbits[i]
#   # print i, list(orbit.lines)[0].direction().value[3]
#   if orbit.moves == set([1, 3, 4, 5, 6, 7, 24, 26, 30, 31, 34, 36, 37, 38, 39, 41, 53, 61, 63, 65, 70, 73, 76, 77, 78, 83, 88, 101, 102, 111]):
#     print i

# print sorted([(i, cell120.cells[i].value[3]) for i in range(120)], key=lambda x: x[1])

# print sorted([i for i in range(120)], key=lambda i: cell120.cells[i].value[3])

# l = [(i, list(x.lines)[0].direction().value[3]) for i, x in enumerate(cell120.edge_orbits)]
# for i in l:
#   print i

# l = [13, 18, 22, 24, 25] # A circle of second layer cells
# l = [7, 8, 12, 18, 19, 25, 26, 28, 31] # A cluster of three first layer cells, around one dodecahedral vertex, and six second layer cells from six vertices on the three pentagons but not adjacent to the central vertex
# l = [0, 1, 2, 8, 10, 11, 12, 13, 14, 18, 19, 21, 24, 25, 30, 31, 32, 34, 35]
# l = [5, 9, 10, 12, 21, 23, 25, 27, 28, 29, 30, 32, 46, 47, 51, 53]
# for i in l:
#   print i, cell120.cells[i].value

l = [2, 3, 5, 6, 7, 8, 9]
for i in l:
  print i, list(cell120.edge_orbits[i].lines)[0].direction().value


# from matrix_2c import *
# from matrix_3c import *

# matrix_3c_transpose = zip(*matrix_3c)

# intersection_histogram = {}

# column0 = matrix_3c_transpose[0]
# for column in matrix_3c_transpose:
#   intersection = [a * b for a, b in zip(column0, column)].count(1)
#   intersection_histogram[intersection] = intersection_histogram.get(intersection, 0) + 1

# print intersection_histogram

# print '======='
# row0 = matrix_3c[0]
# for row in matrix_3c:
#   intersection = [a * b for a, b in zip(row0, row)].count(1)
#   print intersection.count(1)

