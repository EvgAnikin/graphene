set terminal jpeg
set output 'graphene_spectrum.jpg'

set xrange [-5:5]
set yrange [-5:5]

set isosample 50
set pm3d #map
set size square
set ticslevel 0

f(x,y) = sqrt(3 + 2*(cos(-x/2 + sqrt(3)*y/2)  + \
			cos(x/2 + sqrt(3)*y/2) + \
			cos(x)))

splot f(x,y) title 'Hexahonal lattice spectrum' linecolor rgb "#FF3030"
