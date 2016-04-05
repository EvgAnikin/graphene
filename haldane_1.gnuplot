set terminal jpeg
set output 'haldane.jpg'

t = 1
t2 = 0.2
vy = sqrt(3)/2

a(y) = 4*t2*sin(vy*y)
b(y) = -4*t2*sin(vy*y)*cos(vy*y) + 0.5*t**2/t2/tan(vy*y)
c(y) = -0.25*t**4/t2**2/tan(vy*y)**2 + t**2*(1+8*cos(vy*y)**2)

omega(x,y) = sqrt(\
	(4*t2*sin(vy*y)*(cos(1.5*x) - cos(vy*y)) + 0.5*t**2/t2/tan(vy*y))**2 - \
	t**4/4./t2**2/tan(vy*y)**2 + t**2*(1 + 8*cos(vy*y)**2)\
	)

omega1(x,y) = sqrt((a(y)*cos(1.5*x) + b(y))**2 + c(y))

omega2(x,y) = sqrt(\
	(4*t2*sin(vy*y)*cos(1.5*x) - 4*t2*sin(vy*y)*cos(vy*y) + 0.5*t**2/t2/tan(vy*y))**2 \
	+c(y) \
	)

w2(x,y) = 4*t2**2*(sin(1.5*x + vy*y) - sin(2*vy*y) - sin(1.5*x - vy*y))**2 + \
		t**2*(3 + 2*(cos(1.5*x + vy*y) + cos(2*vy*y) + cos(1.5*x - vy*y)))

set xrange[0:4*pi/3]
set yrange[0.01:2*pi/vy-.01]
set zrange[:3]
set isosample 50 
#set pm3d
set contour base
#splot sqrt(w2(x,y))
splot omega1(x,y)#, omega2(x,y)
