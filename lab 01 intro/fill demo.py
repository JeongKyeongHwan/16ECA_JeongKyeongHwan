#-*- coding: utf8 -*-

import numpy as np

x = np.linspace(0, 1, 500)

y = np.sin(10 * 2 * np.pi * x) * np.exp(-5 * x)

plt.fill(x, y, 'r')

plt.grid(Ture)

plt.show()
