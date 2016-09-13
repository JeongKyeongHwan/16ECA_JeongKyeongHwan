#-*- coding: utf8 -*-

from pylab import *

import matplotlib.pyplot as plt

x = randn(100000)
y = randn(100000) + 5

H, xedges, yedges = histogram2d(x, y, bins=40)

extent = (yedges[0], yedges[-1], xedges[-1], xedges[0])

plt.imshow(H, extent=extent, interpolation='nearest')

show()

# http://matplotlib.org/examples/pylab_examples/hist2d_log_demo.html