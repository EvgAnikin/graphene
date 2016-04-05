import sys
import matplotlib.pyplot as plt
import scipy.optimize as sopt
from a_edge_states import *

t = 1
t2 = 0.2
py = float(sys.argv[1])
epsilon = 1e-2
omega_max = spectrum_edge(t,t2,py) - epsilon

omegas = np.linspace(-omega_max, omega_max, 500)

plt.plot(omegas, map(lambda omega : detG(t,t2,omega,py).real, omegas))
plt.plot(omegas, map(lambda omega : detG(t,t2,omega,py).imag, omegas))
plt.plot(omegas, [0]*len(omegas))
plt.xlim(-omega_max,omega_max)
#plt.ylim(-0.005,0.005)
print a(t,t2,py), b(t,t2,py), c(t,t2,py)
plt.show()
