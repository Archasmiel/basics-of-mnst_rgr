from info import task5
from math import *

var = open('../variant.txt', 'r').readline().strip()
inf, material, L, W, H = task5.get(var)

C1 = 1.421 if inf == 'mis' else 1.875
tef = 18.1e-6

E = material.get('E')
ro = material.get('ρ')

a, b = H, W

f01 = ((C1**2)/(4*pi*sqrt(3))) * sqrt(E/ro) * (a/L/L)
kef = 4*E*(a**3)*b/(L**3) if inf == 'mis' else E*(a**3)*b/(L**3)/4
w01 = 2*pi*f01
Q = kef/(tef*w01)

print(f'f01 = {f01}')
print(f'kеф = {kef}')
print(f'Q = {Q}')
