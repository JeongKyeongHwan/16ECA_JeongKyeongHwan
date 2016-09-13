#-*- coding: utf8 -*-
"""
Simple demo of the fill function
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
# x data 생성 : 0부터 1사이를 500구간으로 나눔

y = np.sin(10 * 2 * np.pi * x) * np.exp(-5 * x)
# y deta생성 : exp()함수와 sin()함수의 곱으로 생성
# x와 같은 수의 data를 생성함
# >>> print len(x)
# >>> print len(y)
# 위 두 결과가 같을 것임

plt.fill(x, y, 'r')
# 그래프를 그리고 x축과의 사이를 'r'에 따라 빨간 색으로 칠함
plt.grid()
#모눈 생성
plt.show()
#그래프를 화면의 표시
