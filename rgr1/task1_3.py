import numpy as np

from info import task1_3

var = open('../variant.txt', 'r').readline().strip()
material, X, Y, Z, dx, dy, dz = task1_3.get(var)
E = material.get('E')
t = material.get('μ')

Sxy, Sxz, Syz = X*Y, X*Z, Y*Z

e_x = dx/X
e_y = dy/Y
e_z = dz/Z
print(f'εx = {e_x}')
print(f'εx = {e_y}')
print(f'εx = {e_z}')

A = np.array([[1, -t, -t], [-t, 1, -t], [-t, -t, 1]])
B = np.array([[e_x*E], [e_y*E], [e_z*E]])
res = np.linalg.inv(A).dot(B)
print(f'A = {A}')
print(f'X = {res}')
print(f'B = {B}')

s_x = res[0][0]
s_y = res[1][0]
s_z = res[2][0]
print(f'σx = {s_x}')
print(f'σy = {s_y}')
print(f'σz = {s_z}')

Fx = s_x*Syz
Fy = s_y*Sxz
Fz = s_z*Sxy
print(f'Fx = {Fx}')
print(f'Fy = {Fy}')
print(f'Fz = {Fz}')

