import matplotlib.pyplot as plt
import scipy.optimize as spo
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from a_edge_states import *

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#
#py = np.linspace(0,2*pi/sqrt(3),70)
#omega = np.linspace(-0.4,0.4,50)
#py,omega = np.meshgrid(py,omega)
#
#surf = ax.plot_surface(py, omega, detG(py,omega).real, rstride=1, cstride=1, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
#ax.plot_wireframe(py,omega,detG(omega,py), rstride=1, cstride=1)
##ax.plot_surface(py,omega,0, rstride=1, cstride=1, color='red')
#ax.set_zlim((-0.01,0.01))
#fig.show()


def plot_slice_py(py):
	omega = np.linspace(-3,3, 200)
	plt.plot(omega, detG(t,t2,omega,py).real)
	plt.plot(omega, detG(t,t2,omega,py).imag, color = 'green')
	plt.xlim((-1,1))
	plt.ylim((-1,1))
	plt.show()

def plot_slice_omega(omega):
	pymin = 0
	pymax = 2*pi/sqrt(3)
	py = np.linspace(pymin,pymax, 500)
	
#	plt.plot(py, GreenFunctions(t,t2,omega,py)[0].real)
#	plt.plot(py, GreenFunctions(t,t2,omega,py)[1].real)
#	plt.plot(py, GreenFunctions(t,t2,omega,py)[3].real)
	plt.plot(py, detG(t,t2,omega,py).real)
#	plt.plot(py, c(t,t2,py), color = 'orange')
	plt.xlim((pymin,pymax))
	plt.ylim((-0.1,0.1))
	plt.show()

plot_slice_omega(0)

#omegas = np.linspace(0.001,0.15,30)
#pys = []
#npys = []
#for omega in omegas:
#	new_py = spo.brentq(lambda py : detG(omega,py).real, pi/sqrt(3), 2*pi/sqrt(3) - 1)
#	pys.append(new_py)
#	npys.append(2*pi/sqrt(3) - new_py)
#
#plt.plot(pys, omegas, color = 'r') 
#plt.plot(pys, -omegas, color = 'r')
#plt.plot(npys, omegas, color = 'r') 
#plt.plot(npys, -omegas, color = 'r') 
#plt.show()
