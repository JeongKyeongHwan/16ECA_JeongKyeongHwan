epsilon_global = 1e-4

def newton(f, x0, epsilon=epsilon_global, b_verbose=False):

    xi = float(x0)

    counter = 0

    while True:
        fi = f(xi)

        if abs(fi) < epsilon:
            break

        else:
            xi += ((2 - x0 * x0) / (2 * x0))

        return xi

def func(x):

    return 1.0 * x * x - 2.0

def main():

    x_nr = newton(func, 1.4, b_verbose=True)
    print 'x_nr =', x_nr
    print "f(x_nr) =", func(x_nr)

if "__main__" == __name__:
    main()
