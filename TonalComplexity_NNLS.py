import numpy
import math
import cmath
from scipy.io import loadmat

"""#chroma toolbox
clp_mat = loadmat('MATLAB-Chroma-Toolbox_2.0\\MATLAB-Chroma-Toolbox_2.0\\data_CLP\\Bach_BWV988-Aria-Measures1-4_Meinard_fast.mat')
clp1 = clp_mat['f_logchroma_norm']
clp2 = numpy.transpose(clp1)
#L1 normnized
l1_norms = numpy.sum(numpy.abs(clp2), axis=1)
clp = clp2 / l1_norms[:, numpy.newaxis]
#print(clp)"""

#NNLS
clp1 = numpy.genfromtxt('NNLS\\Systematic_Cadence-C-Major_Meinard_portato.csv', delimiter=',')
new_order = [3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
clp = clp1[:, new_order]

#clp = numpy.array([[1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12]])

def entropy(c):
    n = len(c)
    e = 0
    for i in range(0,n):
        cn = c[i]
        e += cn * math.log2(cn)
    e = -e / math.log2(n)
    return e

def flat(c):
    n = len(c)
    flat1 = 1
    flat2 = 0
    for i in range(0,n):
        cn = c[i]
        flat1 *= cn
    flat1 =  pow(flat1, 1/n)
    for i in range(0,n):
        cn = c[i]
        flat2 += cn
    flat2 = flat2 / n
    flat = flat1 / flat2
    return flat

def fifth_c(c):
    n = len(c)
    fifth_c = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,n):
        fifth_n = (i * 7) % 12
        fifth_c[i] = c[fifth_n]
    return fifth_c

def tonal_complexity_caculation(fifthc):
    n = len(fifthc)
    r = 0
    for i in range(0,n):
        c_fifth_n = fifthc[i]
        #r += c_fifth_n * cmath.exp(2 * cmath.pi * 1j * i / 12)
        length = c_fifth_n * cmath.exp(2 * cmath.pi * 1j * i / 12)
        r += length
        #print(length)
        #print(c_fifth_n)
        #print(r)
        #print("\n")
    r = abs(r)
    fifth = pow(1-r,1/2)
    if numpy.isnan(fifth):
        print(r)
    return fifth

"""#Entropy
entropy_list = []
for c in clp:
    e = entropy(c)
    entropy_list.append(e)
print (entropy_list)
entropy_average = numpy.mean(entropy_list)
print(entropy_average)"""

#Flat
flat_list = []
for c in clp:
    f = flat(c)
    flat_list.append(f)
#print(flat_list)
flat_average = numpy.mean(flat_list)
#print(flat_average)

#Fifth_c
fifthc = []
for c in clp:
    fifth = fifth_c(c)
    fifthc.append(fifth)
fifth_croma = numpy.array(fifthc)
#print(fifth_croma)

#Fifth 
fifth_list = []
for fc in fifth_croma:
    f = tonal_complexity_caculation(fc)
    fifth_list.append(f)
#print(fifth_list)
tonal_complexity_average = numpy.mean(fifth_list)
print(tonal_complexity_average)