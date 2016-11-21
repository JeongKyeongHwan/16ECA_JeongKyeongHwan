#-*- coding: utf8

"""
벡터 클래스
python의 list를 확장하여 벡터를 구현하고자 함
"""

import itertools

class Vector(list):
    # list를 상속
    # list의 대부분의 기능 (__getitem__ 등)을 그대로 사용
    def __add__(self, other):
        """덧셈"""
        if len(self) == len(other):
            result = Vector([s + o for s, o in itertools.izip(self, other)])
        else:
            raise ValueError("Vector size mismatch")
        return result

    def __mul__(self, other):
        """스칼라 벡터 곱셈 또는 벡터 내적"""
        if isinstance(other, (int, float, complex)):
            """scala vector product"""
            result = Vector([s * other for s in self])
        elif isinstance(other, Vector):
            """dot product"""
            if len(self) == len(other):
                # 두 벡터의 길이가 같을 경우
                result = 0.0
                for s, o in itertools.izip(self, other):
                    result += s * o
            else:
                # 두 벡터의 길이가 다를 경우
                raise ValueError("Vector size mismatch")
        else:
            # 스칼라 곱도 벡터 내적도 아닌 것으로 보이는 경우
            raise TypeError("Not defined")
        return result

    def __rmul__(self, other):
        # Q : 이 함수의 역할은 무엇인가?
        return self * other


    def __abs__(self):
        """벡터의 크기 magnitude"""
        # 제곱의 합
        sqare_sum =  self * self
        # 제곱의 합의 제곱근
        result = sqare_sum ** 0.5
        return result

    def __pow__(self, power, modulo=None):
        """element-wise power"""
        return Vector([s ** power for s in self])

# Q : vector 모듈에는 있으나 Vector 클래스에는 없는 기능을 구현해 보시오

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    def main():
        # SungHo Hwang, Hahn & Valentine, Essential MATLAB for Engineers and Scientists 3/e,
        # Korean Version, A_Jin, 2008, p. 32
        x = Vector([1, 3, 0, -1, 5])
        print(x)
        print(dir())
        a = Vector([5, 6, 7])
        print(a)

        # SungHo Hwang, Hahn & Valentine, Essential MATLAB for Engineers and Scientists 3/e,
        # Korean Version, A_Jin, 2008, p. 39
        g = - 9.8
        u = 60
        t = Vector(range(0, 123)) * 0.1
        s = u * t + g * 0.5 * (t ** 2)
        print s
        plt.plot(t, s)
        plt.show()
    main()

# Q : g = 9.8일때 s 에서 -g를 대입할 경우 실행되는가?