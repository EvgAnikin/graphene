from math import *
import cmath
import numpy as np
from numpy.lib import scimath

VY = sqrt(3)/2

def a(t,t2,py):
	return 4*t2*np.sin(VY*py)

def b(t,t2,py):
	return -4*t2*np.sin(VY*py)*np.cos(VY*py) + \
			0.5*t**2/t2/np.tan(VY*py)
def c(t,t2,py):
	return -0.25*t**4/t2**2/np.tan(VY*py)**2 + \
			t**2*(1 + 8*np.cos(VY*py)**2) 

def energy(t,t2,px,py):
	args = (t,t2,py)
	return (a(*args)*np.cos(1.5*px)+ b(*args))**2 + c(*args)

def GreenFunctions(t,t2,omega,py):
	args = (t,t2,py)
	sqrt_omega_c = scimath.sqrt(omega**2 - c(*args))

	cosk1 = (-b(*args) + sqrt_omega_c)/a(*args)
	cosk2 = (-b(*args) - sqrt_omega_c)/a(*args)

#	if (cosk1.imag == 0 and abs(cosk1) < 1) or (cosk2.imag == 0 and abs(cosk2) < 1):
#		print 'Achtung! We are in spectrum!'

	shk1 = scimath.sqrt(cosk1**2 - 1)
	shk2 = scimath.sqrt(cosk2**2 - 1)

	GAA = (omega - 0.5*t**2/t2/np.tan(VY*py) + sqrt_omega_c)/shk1/sqrt_omega_c\
	-(omega - 0.5*t**2/t2/np.tan(VY*py) - sqrt_omega_c)/shk2/sqrt_omega_c
	
	GBB = (omega + 0.5*t**2/t2/np.tan(VY*py) - sqrt_omega_c)/shk1/sqrt_omega_c\
	-(omega + 0.5*t**2/t2/np.tan(VY*py) + sqrt_omega_c)/shk2/sqrt_omega_c
	
	GAB = t*(2*np.cos(VY*py) + cosk1)/shk1/sqrt_omega_c - \
		t*(2*np.cos(VY*py) + cosk2)/shk2/sqrt_omega_c
	GBA = GAB.conjugate()

	return (GAA, GAB, GBA, GBB)

def detG(t,t2,omega,py):
	GAA, GAB, GBA, GBB = GreenFunctions(t,t2,omega,py)
	return GAA*GBB - GAB*GBA

def spectrum_edge(t,t2,py):
	if abs(b(t,t2,py)/a(t,t2,py)) < 1:
		return sqrt(c(t,t2,py))

	omega1 = sqrt(c(t,t2,py) + (a(t,t2,py) + b(t,t2,py))**2)
	omega2 = sqrt(c(t,t2,py) + (a(t,t2,py) - b(t,t2,py))**2)
	return min(omega1, omega2)
