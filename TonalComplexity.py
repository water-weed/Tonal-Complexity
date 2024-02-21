import numpy
import math
import cmath

c = numpy.array([[0,0,0,0,0,0,0,0,0,0,0,0]])

#normalize
l1_norm = numpy.sum(numpy.abs(c))
normalized_c = c / l1_norm

#Entropy
n = numpy.linalg.norm(normalized_c)[0]
entroy = 0
for i in range(0,n):
    cn = normalized_c[0][i]
    entroy += cn * math.log2(cn)
entroy = -entroy / math.log2(n)

#Flat
flat1 = 1
flat2 = 0
for i in range(0,n):
    cn = normalized_c[0][i]
    flat1 *= cn
flat1 =  pow(flat1, 1/n)
for i in range(0,n):
    cn = normalized_c[0][i]
    flat2 += cn
flat2 = flat2 / n
flat = flat1 / flat2

#Fifth
fifth_c = numpy.array([[0,0,0,0,0,0,0,0,0,0,0,0]])
for i in range(0,n):
    fifth_n = (i * 7) // 12
    fifth_c[0][i] = normalized_c[0][fifth_n]
r = 0
for i in range(0,n):
    c_fifth_n = fifth_c[0][i]
    r += c_fifth_n * cmath.exp(2j * cmath.pi * i / 12)
r = abs(r)
fifth = pow(1-r,1/2)

