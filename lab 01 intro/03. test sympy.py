#-*- coding: utf8 -*-
# http://docs.python.org/2.7/library/stdtypes.html#string-formatting

# symbolic processor 기능을 가진 sympy 를 불러 들여 sp라는 이름에 연결시킴
import sympy as sp

x, y = sp.symbols('x y')
# 심파이 심볼기능으로 기호 x y를 정함

z = x + 2 * y

print('z = %s' % z)

# Sympy Tutorial, http://docs.sympy.org/latest/tutorial/index.html