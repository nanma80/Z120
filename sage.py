# http://aleph.sagemath.org/?z=eJzzDVawVfBNLCnKrAguSExO1XB30zDS1FEwBiJNXq7yjMycVIWQotJUK14uBSDwBSkP1itKzEvJz41PzUnNTc0r0dCESGamKfjqZRbHZ-aVpRaVZCblpGpoQvWBQFJRamI2gsvLVVCUmVeioO5rpQ5j-yIEgYYgieuBzSxOBVkFU6GFpkZBC1UdABH6PRM=&lang=sage

MS = MatrixSpace(GF(2), 2, 3)

A = MS([1, 0, 0,    1, 1, 1])

V = VectorSpace(GF(2), 2)

y = V([1, 0])

x = A.solve_right(y)

view(A)

view(y.column())

view(x.column())
