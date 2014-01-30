from cell120 import *

c = Cell120()

# for c0 in c.cells:

#   count = 0

#   for v in c.vertices:
#     distance = c0.distance_to(v)
#     if distance < 0.149:
#       count += 1

#   print count

# print len(c.edges)
# e0 = c.edges[0]
# count = 0

# for c in c.cells:
#   distance = e0.center().distance_to(c)
#   if distance < 0.1306:
#     print c.value
#     count += 1

# print count


# c.edge_orbits

# edge_directions = [edge.direction() for edge in c.edges]

# print len(edge_directions)
# print len(set(edge_directions))

# orbits = {}
# for edge in c.edges:
#   orbits[edge.direction()] = edge
# print len(orbits)


# face_directions = [face.direction() for face in c.faces]

# print len(face_directions)
# print len(set(face_directions))
# s = set(face_directions)
# print [d.value for d in s]

# c0 = c.cells[119]
# count = 0

# for c in c.edges:
#   distance = c0.distance_to(c.center())
#   if distance < 0.1306:
#     count += 1

# print count

# minimum = 100

# for c in c.edges:
#   distance = c0.distance_to(c.center())
#   print distance
#   if distance > 0 and distance < minimum:
#     minimum = distance

# print minimum


# count = 0

# for c in c.cells:
#   distance = c0.distance_to(c)
#   if distance < 0.382:
#     count += 1

# print count

# minimum = 100

# for c in c.cells:
#   distance = c0.distance_to(c)
#   print distance
#   if distance > 0 and distance < minimum:
#     minimum = distance

# print minimum

# v0 = c.vertices[0]

# count = 0

# for v in c.vertices:
#   distance = v0.distance_to(v)
#   if distance < 0.073:
#     count += 1

# print count