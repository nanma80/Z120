# This file was *autogenerated* from the file rank.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_43 = Integer(43); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_55 = Integer(55); _sage_const_74 = Integer(74); _sage_const_65 = Integer(65); _sage_const_57 = Integer(57); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_59 = Integer(59); _sage_const_56 = Integer(56); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_32 = Integer(32); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_54 = Integer(54); _sage_const_68 = Integer(68); _sage_const_52 = Integer(52); _sage_const_33 = Integer(33); _sage_const_58 = Integer(58); _sage_const_70 = Integer(70); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_63 = Integer(63); _sage_const_66 = Integer(66); _sage_const_69 = Integer(69); _sage_const_67 = Integer(67); _sage_const_53 = Integer(53); _sage_const_64 = Integer(64); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_39 = Integer(39); _sage_const_62 = Integer(62); _sage_const_71 = Integer(71); _sage_const_60 = Integer(60); _sage_const_73 = Integer(73); _sage_const_38 = Integer(38); _sage_const_61 = Integer(61); _sage_const_72 = Integer(72)
sage.misc.preparser.load(sage.misc.preparser.base64.b64decode("bWF0cml4XzNjLnB5"),globals(),False)

def matrix_gf2_rank(matrix):
  n_rows = len(matrix)
  n_columns = len(matrix[_sage_const_0 ])
  MS = MatrixSpace(GF(_sage_const_2 ), n_rows, n_columns)
  matrix_gf2 = MS(matrix)
  return matrix_gf2.rank()

matrix_3c_skipped = matrix_3c[_sage_const_2 :_sage_const_48 ]
# matrix_3c_skipped = matrix_3c[0:60]
print 'Selecting ' + repr(len(matrix_3c_skipped)) + ' orbits'
matrix = zip(*matrix_3c_skipped)

# matrix = zip(*matrix_3c)
full_rank = matrix_gf2_rank(matrix)
print 'Rank of the full matrix: ' + repr(full_rank)

cells_to_move = []

# core, north pole
cells_to_move += [_sage_const_0 ]

# first layer, 10 cells. Changes 32 orbits
cells_to_move += [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_5 , _sage_const_6 , _sage_const_7 , _sage_const_8 , _sage_const_9 , _sage_const_10 , _sage_const_11 , _sage_const_12 ]

# second layer, 20 cells. Changes 24 orbits
cells_to_move += [_sage_const_13 , _sage_const_14 , _sage_const_15 , _sage_const_16 , _sage_const_17 , _sage_const_18 , _sage_const_19 , _sage_const_20 , _sage_const_21 , _sage_const_22 , _sage_const_23 , _sage_const_24 , _sage_const_25 , _sage_const_26 , _sage_const_27 , _sage_const_28 , _sage_const_29 , _sage_const_30 , _sage_const_31 , _sage_const_32 ]

# third layer, 12 cells. Changes 32 orbits
cells_to_move += [_sage_const_33 , _sage_const_34 , _sage_const_35 , _sage_const_36 , _sage_const_37 , _sage_const_38 , _sage_const_39 , _sage_const_40 , _sage_const_41 , _sage_const_42 , _sage_const_43 , _sage_const_44 ]
# subset of third layer

# fourth layer, equator, 30 cells. Changes 0 orbit
cells_to_move += [_sage_const_45 , _sage_const_46 , _sage_const_47 , _sage_const_48 , _sage_const_49 , _sage_const_50 , _sage_const_51 , _sage_const_52 , _sage_const_53 , _sage_const_54 , _sage_const_55 , _sage_const_56 , _sage_const_57 , _sage_const_58 , _sage_const_59 , _sage_const_60 , _sage_const_61 , _sage_const_62 , _sage_const_63 , _sage_const_64 , _sage_const_65 , _sage_const_66 , _sage_const_67 , _sage_const_68 , _sage_const_69 , _sage_const_70 , _sage_const_71 , _sage_const_72 , _sage_const_73 , _sage_const_74 ]
# subset of equators


# south of equator
# cells_to_move += [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]

# second layer south of equator
# cells_to_move += [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# next to south pole
# cells_to_move += [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]

# south pole
# cells_to_move += [119]

print 'Selecting ' + repr(len(cells_to_move)) + ' moves'
matrix_selected = [matrix[i] for i in cells_to_move]
selected_rank = matrix_gf2_rank(matrix_selected)

print 'Rank of the selected matrix: ' + repr(selected_rank)

if selected_rank == full_rank and len(cells_to_move) == full_rank:
  from cell120 import *
  cell120 = Cell120()
  for cell_index in cells_to_move:
    print cell_index, cell120.cells[cell_index].value
else:
  pass
