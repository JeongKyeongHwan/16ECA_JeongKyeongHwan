#-*- coding: utf8

"""
상미분 방정식 풀이 프로그램을 위한 단위 테스트(unit test)
프로그램이 의도한 대로 작동하는지 확인

시작하기전 파이썬 설정unittest 설정
"""

import itertools

import unittest

import numpy as np

import ode

# 작성한 프로그램을 검증하기 위한 class
# 다른 사람이 만들어 제공해 준 unittest.TestCase 객체에 원하는 기능을 부가하여 만듦
class TestNumericalIntegration(unittest.TestCase):
    def setUp(self):
        # t 구간
        self.ti_sec = 0.0
        self.te_sec = 5.0
        self.delta_t_sec = 0.02
        self.x_init = (0.0, 0.0)

        self.expected_t_sec = np.arange(self.ti_sec, self.te_sec, self.delta_t_sec).tolist()
        self. expected_x0 = [ode.exact(t_sec) for t_sec in self.expected_t_sec]

    def test_mod_euler(self):
        """
        수정 오일러법을 검증
        :return:
        """

        # x(f)의 근사값을 구함
        result_t, result_x = ode.mod_euler(ode.func, self.x_init, self.ti_sec, self.te_sec, self.delta_t_sec)

        # x(t)의 결과값에서 위치, 속도를 각각 x1과 x2로 저장
        result_x1, result_x2 = itertools.izip(*result_x)

        # 예상 값과 결과 값을 하나씩 비교
        for expected, result in itertools.izip(self.expected_x0, result_x1):
            # 예상 값과 결과 값의 오차가 delta이하인지 검증
            self.assertAlmostEqual(expected, result, delta=1e-4)

# 이 script가 import 될 때에는 아래의 코드는 실행되지 않음
if '__main__' == __name__:
    # unit test 실시
    unittest.main()

    # 다른 상미분 방정식 풀이 함수를 검증하는 method를 만들어 보시오
    # 미분 방정식 함수 전체가 아니라 일부만 검증하려면 어떻게 하는 것이 좋겠는가?