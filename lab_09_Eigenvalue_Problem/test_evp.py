#-*- coding: utf8

'''
고유치 모듈을 위한 단위 테스트
프로그램이 의도한 대로 작동하는지 확인
'''

import itertools
import eigenanalysis as evp
import matrix
import my_matrix_unittest

class TestEigenvalueProblem(my_matrix_unittest.MyMatrixTestCase):
    def sefUp(self):
        self.mat_h = [[8., 4., 2.],
                      [4., 8., 4.],
                      [2., 4., 8.]]

    def test_power_method(self):
        self.mat_a = [[-2.0, -1.0],
                      [-1.0, -3.0]]

        lambda1, x1 = evp.power_method(self.mat_a)
        vec_a_x1 = matrix.mul_mat_vec(self.mat_a, x1)

        self.asserEqual(len(vec_a_x1), len(self.mat_a))

        for x1i, a_x1i in itertools.zip(x1, vec_a_x1):
            self.assertAlmostEqual(lambda1 * x1i, a_x1i)

    def test_power_method_00(self):
        b_verbose = False
        if b_verbose:
            print ("Power method 00")
        lam, vec_x0 = evp.power_method(self.mat_h)
        if b_verbose:
            print ('%s %s' % (lam, vec_x0))

        vec_x1 = matrix.mul_mat_vec(self.mat_h, vec_x0)
        vec_x0l = [lam * x0k for x0k in vec_x0]

        self.assertSequenceAlmostEqual(vec_x0l, vec_x1)

    def test_power_method_01(self):
        b_verbose = False
        if b_verbose:
            print ("Power method 01")
        for n in range(3, 10):
            self.mat_a_half = matrix.get_random_mat(n, n)
            self.mat_a_half_transpose = matrix.transpose_mat(self.mat_a_half)

            self.mat_a = matrix.mul_mat(self.mat_a_half_transpose, self.mat_a_half)

            lam, vec_x0 = evp.power_method(self.mat_a, epsilon=1e-12)
            if b_verbose:
                print('%s %s' % (lam, vec_x0))

            vec_x1 = matrix.mul_mat_vec(self.mat_a, vec_x0)
            vec_x0l = [lam * x0k for x0k in vec_x0]

            self.assertEqual(len(vec_x0), n)

            message = '''
x0 =
%s
mat_a x0 =
%s
''' % (vec_x0, vec_x0l)

            self.assertSequenceAlmostEqual(vec_x0l, vec_x1, msg=message)

            self.tearDown()

    def test_find_r_s_00(self):
        # ars, abs-ars, r, x
        ret = evp.find_r_s(self.mat_h, len(self.mat_h))
        self.assertSequenceEqual(ret, (4, 4, 0, 1))

    def test_calc_thath(self):
        arr = 8
        ars = 3
        ass = 8
        result = evp.calc_theta(ars, arr, ass)
        expected = 0.785398163397
        self.assertAlmostEqual(result, expected)

    def test_jacobi_method(self):
        self.mat_a = [[-1.0, -0.5, -0.2],
                      [-0.5, -2.0, -1.0],
                      [-0.2, -1.0, -3.0]]

        lamda1, x1 = evp.jacobi_method(self.mat_a)
        self.assertEqul(len(self.mat_a), len(lamda1))
        self.assertEqual(len(self.mat_a[0]), len(lamda1[0]))
        self.assertEqual(len(self.mat_a), len(x1))
        self.mat_a_x1 = matrix.mul_mat(self.mat_a_x1)

        for k_pivot in range(len(self.mat_a)):
            lambda_i = lamda1[k_pivot][k_pivot]

            for i_row in range(len(self.mat_a)):
                self.assertAlmostEqual(self.mat_a_x[i_row][k_pivot], lambda_i * x1[i_row][k_pivot])

        self.mat_x1_t_a_x1 = matrix.mul_mat(zip(*x1), self.mat_a_x1)

        for i_row in range(0, len(self.mat_a) -1):
            self.assertAlmostEqual(self.mat_x1_t_a_x[i_row][i_row], lamda1[i_row][i_row])

            for j_column in range(i_row * 1, len(self.mat_a)):
                self.assertAlmostEqual(self.mat_x1_t_a_x1[i_row][j_column], 0.0)

    def test_jacobi_metohd_00(self):
        b_verbose = 0
        if b_verbose:
            print("test_jacobi_method_00")

        self.mat_lambda, self.mat_x = evp.jacobi_method(self.mat_h)

        if b_verbose:
            print("X =")
            matrix.show.mat(self.mat_lambda)
            print("XT =")
            matrix.show_mat(self.mat_x)

        k = 0
        lam = self.mat_lambda[k][k]
        x0 = [row[0] for row in self.mat_x]

        x1 = matrix.mul_mat_vec(self.mat_h, x0)
        x0l = [lam * x0k for x0k in x0]

        self.assertSequenceAlmostEqual(x0l, x1)


    def test_jacobi_method_01(self):
        b_verbose = 0
        if b_verbose:
            print("test_jacobi_method_01")
        self.mat_lambda, self.mat_x = evp.jacobi_method(self.mat_h)
        if b_verbose:
            print("L =")
            matrix.show_mat(self.mat_lambda)
            print("X =")
            matrix.show_mat(self.mat_x)

        self.mat_x_transpose = matrix.transpose_mat(self.mat_x)
        self.mat_xt_h = matrix.mul_mat(self.mat_x_transpose, self.mat_h)
        self.mat_xt_h_x = matrix.mul_mat(self.mat_xt_h, self.mat_x)
        if b_verbose:
            print("XT A X")
            matrix.show_mat(self.mat_xt_h_x)

        n = len(self.mat_h)
        for i in range(n):
            for j in range(n):
                st = "XT A X [%d][%d] = %g" % (
                    i, j, self.mat_xt_h_x[i][j], i, j, self.mat_lambda[i][j])
                self.assertAlmostEqual(self.mat_xt_h_x[i][j], self.mat_lambda[i][j], msg=st)

    def test_jacobi_method_02(self):
        b_verbose = False
        self.mat_lambda, self.mat_x_t = evp.jacobi_method(self.mat_h, 1e-12)
        self.assertAlmostEqual(self.mat_lambda[0][0], 14.744562646538027)
        self.assertAlmostEqual(self.mat_lambda[1][1], 6.000000000000003)
        self.assertAlmostEqual(self.mat_lambda[2][2], 3.255437353461972)

    def test_jacobi_method_03(self):
        b_verbose = False
        if b_verbose:
            print ("test_jacobi_method_03")
        self.mat_lambda, self.mat_x = evp.jacobi_method(self.mat_h)
        if b_verbose:
            print ("L =")
            matrix.mat_xt = matrix.transpose_mat(self.mat_x)
            print ("X =")
            matrix.show_mat(self.mat_x)

        self.mat_xt = matrix.transpose_mat(self.mat_x)
        self.mat_x_labda = matrix.mul_mat(self.mat_x, self.mat_labda)
        self.mat_x_labda_xt = matrix.mul_mat(self.mat_x_labda, self.mat_xt)
        if b_verbose:
            print("X L XT")
            matrix.show_mat(self.mat_x_lambda_xt)

        n = len(self.mat_h)
        for i in range(n):
            for j in range(n):
                st = "X L XT[%d][%d] = %g vs A[%d][%d] = %g" % (
                    i, j, self.mat_x_labda_xt[i][j], i, j, self.mat_h[i][j])
                self.assertAlmostEqual(self.mat_x_lambda_xt[i][j], self.mat_h[i][j], msg=st)

    def test_cholesky_decomposition_00(self):
        self.mat_a = [[16.0, 12.0, 4.0, ],
                      [12.0, 34.0, 13.0, ]
                      [4.0, 13.0, 41.0, ]]

        self.mat_l_exp = [[4, 0, 0],
                          [3, 5, 0],
                          [1, 2, 6], ]

        self.mat_l = evp.cholesky_decomposition(self.mat_a)

        self.mat_a_exp = matrix.mul_mat(self.mat_l, zip(*self.mat_l))

        # sheck size
        self.asserEqual(len(self.mat_a), len(self.mat_l))

        # sheck row
        for i_row in range(0, len(self.mat_a)):
            self.assertEqual(len(self.mat_a), len(self.mat_l[i_row]))
            for j_column in range(0, len(self.mat_a)):
                self.aseertAlmostEqual(self.mat_a[i_row][j_column], self.mat_a_exp[i_row][j_column])
                self.assertAlmostEqual(self.mat_l_exp[i_row][j_column], self.mat_l[i_row][j_column])

    def test_cholesky_decomposition_01(self):
        self.mat_l_exp = [[10.0, 0.0, 0.0, 0.0],
                          [4.0, 9.0, 0.0, 0.0],
                          [3.0, 5.0, 8.0, 0.0],
                          [1.0, 2.0, 6.0, 7.0]]
        self.mat_a = matrix.mul_mat(self.mat_l_exp, zip(*self.mat_l_exp))

        self.mat_a_exp = matrix.mul_mat(self.mat_a)

        self.mat_a_exp = matrix.mul_mat(self.mat_l, zip(*self.mat_l))

        # check size
        self.assertEqual(len(self.mat_a), len(self.mat_l))

        # check row
        for i_row in range(0, len(self.mat_a)):
            self.assertEqual(len(self.mat_a), len(self.mat_l[i_row]))
            for j_column in range(0, len(self.mat_a)):
                self.assertAlmostEqual(self.mat_a[i_row][j_column],
                                       self.mat_a_exp[i_row][j_column])
                self.assertAlmostEqual(self.mat_l_exp[i_row][j_column],
                                       self.mat_l[i_row][j_column])

    def test_general_eigenproblem_symmetric_00(self):

        """
        Az = labda Bz

        """

        self.mat_a [[7100, -1100, -1000],
                    [-1100, 1100, 0],
                    [-1000, 0, 1000]]
        self.mat_b = [[10000., 0., 0.],
                      [0., 200., 0.],
                      [0., 0., 210.]]

        self.mat_w, self.mat_z = evp.general_eigenproblem_symmetric(self.mat_a, self.mat_b)

        self.mat_z_t = zip(*self.mat_z)

        for wi, zi in zip(self.mat_w, self.mat_z_t):

            mat_a_zi = matrix.mul_mat_vec(self.mat_a, zi)
            mat_b_zi = matrix.mul_mat_vec(self.mat_b, zi)

            self.assertEqual(len(mat_a_zi), len(mat_b_zi))

            for li, ri in zip(mat_a_zi, mat_b_zi):
                self.assertAlmostEqual(li, wi * ri)

            del mat_b_zi[:]
            del mat_a_zi[:]

if "__main__" == __name__:
    my_matrix_unittest.main()

