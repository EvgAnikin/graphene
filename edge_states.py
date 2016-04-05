#coding=utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt

# eigvalsh - функция, возвращающая собственные значения эрмитовой матрицы

def Hamiltonian(t,t2,N,py):
	Hmlt = np.zeros((2*N,2*N), dtype = np.complex) 
	# Hamiltonian;
	# even indices mean the atoms of B type, odd mean A
	
	z = np.exp(-1j*np.sqrt(3)*py)
	for i in range(1,2*N,2):
		Hmlt[i,i-1] = t*(1 + z)
		Hmlt[i-1,i] = np.conj(Hmlt[i,i-1])
		Hmlt[i,i] = -2*t2*np.sin(np.sqrt(3)*py)
		if i+1 < 2*N:
			Hmlt[i,i+1] = t*z
			Hmlt[i+1,i] =  np.conj(Hmlt[i,i+1])
			Hmlt[i,i+2] = -t2*1j*(1 - z)
			Hmlt[i+2,i] = np.conj(Hmlt[i,i+2])
	
	for i in range(0,2*N,2):
		Hmlt[i,i] = 2*t2*np.sin(np.sqrt(3)*py)
		if i + 2 < 2*N:
			Hmlt[i,i+2] = t2*1j*(1 - z)
			Hmlt[i+2,i] = np.conj(Hmlt[i,i+2])
	return Hmlt

if __name__ == '__main__':
#	try:
#		t,t2 = map(float, sys.argv[1:3])
#		N = int(sys.argv[3])
#	except ValueError, IndexError:
#		print 't, t2, N unset: setting by default'
	t = 1
	t2 = 0.3
	N = 80
	allpy = np.linspace(0, 2*np.pi/np.sqrt(3), 100)
	levels = []
	for py in allpy:
		levels.append(np.linalg.eigvalsh(Hamiltonian(t,t2,N,py)))
	for energies in zip(*levels):
		plt.plot(allpy, energies, 'r-')
	plt.xlim((0,2*np.pi/np.sqrt(3)))
	plt.ylim((-1.5,1.5))
#	plt.ylim((-1,1))
	plt.savefig('levels.jpg')
