#-*- coding: utf8 -*-

epsilon_global = 1e-4
delta_x = 1

def bisection(f, xl, xh, epsilon=epsilon_global, b_verbose=False):

    xl = float(xl)
    xh = float(xl + delta_x)

    xn = xl
    counter = 0

    while True:
        xn = 0.5 * (xl + xh)
        if f(xn) * f(xh) < 0:
            xl = xn
        else:
            xh = xn
        if b_verbose:
            print ('xl = %8f f(xl) = %+8f  xh = %+8f f(xn) = %+8f wh = %+8f f(xh) = %8f Ixh-xlI = %-8f' % (xl, f(xl), xn, f(xn), xh, f(xh), abs(xh - xl)))
        if abs(xh - xl) < epsilon:
            break
    if b_verbose:
        print "bis_counter =", counter
    return xn
def func(x):
    return 1.0 * x * x - 2.0
def dfunc(x):
    return 2.0 * x

x_bis = bisection(func, 1, 1, b_verbose=True)
print 'x_bis=', x_bis
print "f(x_bis) =", func(x_bis)

