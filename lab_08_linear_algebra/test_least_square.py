#-*- coding: utf8
"""
가우스 소거법 모듈을 위한 단위 테스트
프로그램이 의도한 대로 작동하는지 확인
"""

import least_square as ls
import my_matrix_unittest

class TestLeastSquare(my_matrix_unittest.MyMatrixTestCase):
    def test_least_square_fires_order(self):
        vec_x = [0, 1]
        vec_y = vec_x

        self.mat_res = ls.least_square_first_order(vec_x, vec_y)
        self.mat_exp = [[1, 0],
                        [0, 0]]

        self.assertMarixAlmostEqual(self.mat_exp, self.mat_res)

    def test_get_left_inverse_00(self):
        self.mat_x = [[0, 1],
                      [1, 1]]

        self.mat_x_lef_inv = ls.get_left_inverse(self.mat_x)
        self.mat_exp[[-1.000, 1.000],
                     [+1.000, 0.000]]
        self.assertMarixAlmostEqual(self.mat_exp, self.mat_x_left_inv)

    def test_get_left_inverse_01(self):
        self.mat_x = [[0, 0, 1],
                      [1, 1, 1],
                      [4, 2, 1]]
        self.mat_x_lef_inv = ls.get_left_inverse(self.mat_x)
        self.mat_exp = [[+0.5, -1.0, +0.5],
                        [-1.5, +2.0, -0.5],
                        [+1.0, +0.0, +0.0]]

        self.assertMarixAlmostEqual(self.mat_exp, self.mat_x_left_inv)

if __name__ == '__main__':
    my_matrix_unittest.main()
