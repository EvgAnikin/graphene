import matplotlib.pyplot as plt
import scipy.optimize as sopt
import sys
from a_edge_states import *

t = 1
t2 = 0.3
epsilon = 1e-2
pys = list(np.linspace(0+epsilon,2*pi/sqrt(3)-epsilon, 200))
omegas = []
omega_range = 0

for py in pys:
	max_omega = spectrum_edge(t,t2,py) - epsilon
	if max_omega > omega_range:
		omega_range = max_omega
	 
	if detG(t,t2,0,py).real == 0:
		omegas.append(0)
	elif detG(t,t2,0,py).real*detG(t,t2,max_omega,py).real < 0:
		omegas.append(sopt.brentq(lambda om : detG(t,t2,om,py).real, 0, max_omega))
	else:	
#		print detG(t,t2,0,py), detG(t,t2,max_omega,py), py
		omegas.append(float('inf'))

plt.plot(pys,omegas, color = 'red')
plt.plot(pys, map(lambda x : -x, omegas), color = 'red')
plt.xlim((0,2*pi/sqrt(3)))
plt.xlabel('$p_y$')
plt.ylabel('E')
#plt.show()
plt.savefig('edge_kanemele.jpg')
