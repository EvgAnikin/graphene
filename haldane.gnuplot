set terminal jpeg
set output 'haldane_spectrum.jpg'

t = 1
t2 = 0.1

om(x,y) = sqrt(\
	4*t2**2*(2*cos(1.5*x)*sin(sqrt(3)/2*y) - sin(sqrt(3)*y))**2\
	+t**2*(3 + 2*(2*cos(1.5*x)*cos(sqrt(3)/2*y) + cos(sqrt(3)*y)))\
	)

set xrange[0:4*pi/3]
set yrange[0:4*pi/sqrt(3)]
set isosample 50
set contour base
#set pm3d
#set nosurface
splot om(x,y)

#set xrange [0:4*pi/3]
#plot om(x,5)
