import sys
import math
import Image

HEIGHT = 768
WIDTH = 1024
PX,PY = 19e-6, 19e-6
WL = 532e-9

data=[
	(0,0,10),(3,2,15)
]

img=Image.new("L", (WIDTH,HEIGHT), 0)

for j in range(HEIGHT):
	for i in range(WIDTH):
		re = 0.0
		im = 0.0
		for x,y,z in data:
			hx = PX*(i - WIDTH/2) - x
			hy = PY*(j - HEIGHT/2) - y
			th = math.pi/WL*(hx**2+hy**2)/z
			re += math.cos(th)
			im += math.sin(th)
		psi = math.atan2(im,re)
		if psi < 0:
			psi += math.pi*2
#		print psi
		img.putpixel((i,j), psi*255/2/math.pi)
		
img.save(sys.argv[1])
