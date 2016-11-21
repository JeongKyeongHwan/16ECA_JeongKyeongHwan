#-*- coding: utf8
'''
벡터 모듈
python의 list 또는 tuple을 이용하여 벡터를 구현함
'''

from math import sin, cos, pi

def add(x, y):
    """ 벡터 합"""
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = x[k] + y[k]
    return result

print add([5.0, 0.0], (5.0, 0.0))

def scalar_mul(a, x):
    """스칼라 벡터 곱"""
    result = [0.0] * len(x)
    for k in xrange(len(x)):
        result[k] = a * x[k]
    return result

print scalar_mul(10, [1.0, 1.0])
print scalar_mul(10, range(0, 10))

def dot(x, y):
    """벡터 내적"""

    # 백터 x의 크기
    n = len(x)

    # 벡터 y 의 크기는 같을 것이라고 가정한다.
    # Q : 이대로 벡터의 내적을 계산해도 괜찮을 것인가?

    # 내적으 ㄹ계산한 결과를 저장할 변수
    result = 0.0

    # elememt loop
    # x[] y[] 두 리스트의 각 요소들 낄 곱하여 result 에 누산 accmulate 한다.
    for i in range(n):
        result += x[i] * y[i]
    # 누산 결과를 반환
    return result

print dot([1.0, 1.0], [1.0, 1.0])

def mag(x):
    """벡터의 크기"""
    return (dot(x, x)) ** (0.5)

print mag((1.0, 1.0))

def cross2d(x, y):
    """2차원 벡터의 외적"""
    return 0.0, 0.0, x[0] * y[1] - x[1] * y[0]

print cross2d([10.0, 1.0], [5.0, 3.0])

a = [1.0, 3.0]
b = [5.0, 7.0]
print cross2d(a, b)

def rot2d(r, theta_deg):
    """벡터 회전"""
    x = r[0]
    y = r[1]
    theta_rad = theta_deg * pi / 180
    c = cos(theta_rad)
    s = sin(theta_rad)
    return c * x - s * y, s * x + c * y

print rot2d([1.0, 1.0], 30)

# Q : 벡터 클래스의 그래프 에제를 재현해 보시오. 필요하면 함수를 추가하시오.