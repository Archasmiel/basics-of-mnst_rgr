
E = 270e9
torr = 0.31

Fx = -28e-6
Fy = 0.428
Fz = -54.77

x = 600e-6
y = 4e-6
z = 0.7e-6

Sxy = x*y
Syz = y*z
Sxz = x*z

sig_x = Fx/Syz
sig_y = Fy/Sxz
sig_z = Fz/Sxy

epsi_x = (sig_x - torr*sig_y - torr*sig_z)/E
epsi_y = (sig_y - torr*sig_x - torr*sig_z)/E
epsi_z = (sig_z - torr*sig_y - torr*sig_x)/E

print(" {:.9f}".format(epsi_x*x))
print(" {:.9f}".format(epsi_y*y))
print("{:.9f}".format(epsi_z*z))
