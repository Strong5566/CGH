from __future__ import division
import sys
from PIL import Image
from numpy import *
import numpy

level=200
cir=50

im=Image.open(sys.argv[1]).convert("L")
pc=array(im)
pc=double(pc)
pc=fft.fftshift(pc)
pc=pc/pc.max()
w, h=im.size

xx=random.rand(h,w)*2*pi*1j

Kinoform=exp(xx)
for it in range(cir):
    Ft=fft.fft2(Kinoform)
    Pang=angle(Ft)
    Pph=exp(1j*Pang)
    Fn=multiply(Pph, pc)
    CGHs=fft.ifft2(Fn)
    NAng=numpy.round((angle(CGHs)/2/pi+0.5)*level)
    Kinoform=exp(1j*NAng*2*pi/level);
    Fn=abs(Ft)
    c=Fn.sum()/pc.sum();
    Fn=abs(2*c*pc)-abs(Ft)
    Fn=multiply(Fn, Pph)
    huan=(fft.ifft2(Fn))
    NAng=numpy.round((angle(huan)/2/pi+0.5)*level);
    Kinoform=exp(1j*NAng*2*pi/level)

CGH=(NAng/level)

o=(CGH*255).astype(uint8)
om = Image.fromstring("L", (o.shape[1], o.shape[0]), o.tostring())
# om = om.transpose(Image.FLIP_LEFT_RIGHT)
om.save(sys.argv[2])

rec=fft.ifft2(Kinoform)
Rec=fft.fftshift(abs(power(rec, 2)))
Nm=Rec.max()
RecF=Rec/Nm;

o2=(RecF*255).astype(uint8)
om2 = Image.fromstring("L", (o2.shape[1], o2.shape[0]), o2.tostring())
om2.save(sys.argv[3])