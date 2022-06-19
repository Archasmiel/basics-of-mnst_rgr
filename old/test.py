import numpy as np

E = 270e9
t = 0.31

x = 600e-6
y = 4e-6
z = 0.7e-6

Sxy = x*y
Syz = y*z
Sxz = x*z

d_x = 15e-6
d_y = 0.12e-6
d_z = -0.06e-6

# sig_x = Fx/Syz
# sig_y = Fy/Sxz
# sig_z = Fz/Sxy

epsi_x = d_x/x
epsi_y = d_y/y
epsi_z = d_z/z


A = np.array([[1, -t, -t], [-t, 1, -t], [-t, -t, 1]])
inv_A = np.linalg.inv(A)
B = np.array([[epsi_x*E], [epsi_y*E], [epsi_z*E]])
X = inv_A.dot(B)

print(A)
print(X[0][0]*Syz)
print(X[1][0]*Sxz)
print(X[2][0]*Sxy)
print(B)

print(epsi_x)
print(epsi_y)
print(epsi_z)
