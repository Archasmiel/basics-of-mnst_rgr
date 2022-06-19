from info import task1_1

var = open('../variant.txt', 'r').readline().strip()
material, X, Y, Z, Fx = task1_1.get(var)
E = material.get('E')
t = material.get('μ')

Sxy, Sxz, Syz = X*Y, X*Z, Y*Z

s_x = Fx / Syz
print(f'σx = {s_x}')

e_x = s_x/E
e_y = -t*s_x/E
e_z = -t*s_x/E
print(f'εx = {e_x}')
print(f'εy = {e_y}')
print(f'εz = {e_z}')

dx = X*e_x
dy = Y*e_y
dz = Z*e_z
print(f'∆x = {dx}')
print(f'∆y = {dy}')
print(f'∆z = {dz}')

