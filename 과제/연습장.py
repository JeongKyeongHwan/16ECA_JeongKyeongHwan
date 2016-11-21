#-*- coding: utf8
import matplotlib.pyplot as plt
def scalar_mul(a, x):
    """스칼라 벡터 곱"""
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = a * x[k]
    return result
def scalar_mul02(a, x):
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = a[k] * x[k]
    return result
def scalar_mul03(a, x):
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = a[k] - x[k]
    return result
print scalar_mul03([0.1, 0.1], [0.2, 0.3])
def vec():

    g = 9.8
    u = 60
    t = scalar_mul(0.1, range(0, 123))
    print t
    t1 = scalar_mul(0.1 * u, range(0, 123))
    print t1
    t2 = scalar_mul02(t, t)
    print t2
    t3 = scalar_mul(g * 0.5, t2)
    s = scalar_mul03(t1, t3)
    print s
    plt.plot(t, s)
    plt.show()

vec()



