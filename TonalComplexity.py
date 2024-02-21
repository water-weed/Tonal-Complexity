import numpy

c = numpy.array([[0,0,0,0,0,0,0,0,0,0,0,0]])

#normalize
l1_norm = numpy.sum(numpy.abs(c))
normalized_c = c / l1_norm

#