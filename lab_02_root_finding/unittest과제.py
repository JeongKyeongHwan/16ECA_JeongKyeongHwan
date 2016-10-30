#-*- coding: utf8 -*-

import unittest

import root_finding as rf

def f(x):

    x_float = float(x)

    return (x_float ** 0.5) - 2.0

def dfdx(x):

    x_float = float(x)

    return 0.5 / (x_float ** 0.5)

class TestRootFinding(unittest.TestCase):

    def test_sequential(self):
        result = rf.sequential(f, 2.0, 1e-4)
        self.assertAlmostEqual(0.0, f(result), places=3)

    def test_bisection(self):
        result = rf.bisection(f, 0.0001, 100, epsilon=1e-8)
        self.assertAlmostEqual(0.0, f(result), places=3)

    def test_newton(self):
        result = rf.newton(f, dfdx, 0.0001, epsilon=1e-8)
        self.assertAlmostEqual(0.0, f(result), places=3)

if '__main__' == __name__:
    unittest.main()