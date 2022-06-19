from info import task1_2

var = open('../variant.txt', 'r').readline().strip()
material, X, Y, Z, Fx, Fy = task1_2.get(var)
E = material.get('E')
t = material.get('μ')

Sxy, Sxz, Syz = X*Y, X*Z, Y*Z

s_x = Fx / Syz
s_y = Fy / Sxz
print(f'σx = {s_x}')
print(f'σy = {s_y}')

e_x = (s_x - t*s_y)/E
e_y = (s_y - t*s_x)/E
e_z = (-t*s_x - t*s_y)/E
print(f'εx = {e_x}')
print(f'εy = {e_y}')
print(f'εz = {e_z}')

dx = X*e_x
dy = Y*e_y
dz = Z*e_z
print(f'∆x = {dx}')
print(f'∆y = {dy}')
print(f'∆z = {dz}')

