import sys
import struct
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

SIZEOF_INT=4
SIZEOF_FLOAT=4

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

f=open(sys.argv[1], "rb")
n=struct.unpack("i", f.read(SIZEOF_INT))[0]

dat=[]
for i in range(n):
	x,y,z=struct.unpack("fff", f.read(SIZEOF_FLOAT*3))
	if i%10!=0:
		continue
	ax.scatter(x, y, z)

plt.show()
