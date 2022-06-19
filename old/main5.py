
from math import *




s = 'm'  # konsolna/mistkova

E = 130e9
ro = 2320

tef = 18.1e-6
C1 = 1.421 if s == 'm' else 1.875

L = 600e-6
W = 4e-6
H = 0.7e-6

a = H
b = W

f01 = ((C1**2)/(4*pi*sqrt(3))) * sqrt(E/ro) * (a/L/L)
kef = 4*E*(a**3)*b/(L**3)
w01 = 2*pi*f01
Q = kef/(tef*w01)


print(f'f01 = {f01}')
print(f'kеф = {kef}')
print(f'Q = {Q}')
