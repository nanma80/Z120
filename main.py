from cell120 import *

cell120 = Cell120()

print sorted([(i, cell120.cells[i].value[3]) for i in range(120)], key=lambda x: x[1])

print sorted([i for i in range(120)], key=lambda i: cell120.cells[i].value[3])



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

