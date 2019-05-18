m = 120 #kg
g = 9.8 #m/s
M = 5 #kg
L = 0.48 #m

V1 = m*g/2
V2 = m*g/4
V3 = m*g/4
w = M*g/L

By = (w*L**2 + V2*0.18 + V3*L)/L
Ay = V1+V2+V3*w*L-By

print(Ay,By)