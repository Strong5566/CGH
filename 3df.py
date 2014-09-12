import sys
import struct
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import ctypes

SIZEOF_INT=ctypes.sizeof(ctypes.c_int)
SIZEOF_FLOAT=ctypes.sizeof(ctypes.c_float)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

f=open(sys.argv[1], "rb")
n=struct.unpack("i", f.read(SIZEOF_INT))[0]

dat=[]
for i in range(n):
	x,y,z=struct.unpack("fff", f.read(SIZEOF_FLOAT*3))
	if i%100!=0:
		continue
	ax.scatter(x, y, z)

plt.show()
