import gD as gD
from engine import Value
def f(p):
    [x, y, z] = p
    return (x-1)**2+(y-2)**2+(z-3)**2
    # return (x-2)**2+3*(y-0.5)**2+(z-2.5)**2
    # return x*x + 3*y*y + z*z - 4*x - 3*y - 5*z + 8

p = [Value(0.0), Value(0.0), Value(0.0)]
gD.gradientDescendent(f, p)
