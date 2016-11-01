#-*- coding: utf8

"""
수치 적분 프로그램을 위한 단위 테스트(unit test)
프로그램이 의도한 대로 작동하는지 확인

시작하기전 파이참 설정 >>> test_root_finding 참고

"""

import math
import unittest

import num_int

def f(theta_rad):
    """
    정적분을 구하고자 하는 함수
    :param thata_rad: float radian
    :return:
    """
    # 매개변수 x가 실수가 아닐 수도 잇으므로 실수로 변환
    theta_red_float = float(theta_rad)

    return math.sin(theta_red_float)

def integrated_f(theta_rad):
    """
    f() 함수의 부정적분, 적분 상수는 0으로 가정정
    param theta_rad:
    :return:
    """

    # 매개변수 x가 실수가 아닐 수도 있으모로 실수로 변환
    theta_rad_float = float(theta_rad)

    return -math.cos(theta_rad_float)


# 작성한 프로그램을 검증하기 위한 class
# 다른 사람이 만들어 제공해 준 unittest. TestCase 객체에 원하는 기능을 부가하여 만듦

class TestNumericalIntegration(unittest.TestCase):
    def setUp(self):
        # 적분 구간
        self.xi_rad = 0.0
        self.xe_rad = 2.0 * math.pi

        # 정적분의 정의에 따라 예상 값을 계산
        self.expected = integrated_f(self.xe_rad) - integrated_f(self.xi_rad)

    def test_rect(self):
        """
        0차 적분 함수를 검증
        :return:
        """

        # 함수의 정적분을 구함
        result = num_int.rect0(f, self.xi_rad, self.xe_rad, 360)

        self.assertAlmostEqual(self.expected, result, places=6)

    def test_trapezoid(self):
        """
        1차 적분 함수를 검증
        :return:
        """

        # 함수의 정적분을 구함
        result = num_int.trapezoid1(f, self.xi_rad, self.xe_rad, 360)

        self.assertAlmostEqual(self.expected, result, places=6)

# 이 script가 import 될 때는 아래의 코드는 실행되지 않음
if '__main__' == __name__:
    # unit test 실시
    unittest.main()

    # 2차 적분 검증 method를 만들어 보시오
