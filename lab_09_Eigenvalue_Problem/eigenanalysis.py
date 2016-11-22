#-*- coding: utf8

'''
고유 해석 모듈
python의 list의 list를 이용하는 행렬로 구현함
'''

import math

import gauss_jordan as gj
import matrix

def power_method(mat_a, epsilon=1e-9, b_verbose=False):
    # 행렬의 크기
    n = len(mat_a)

    #가장 큰 고유치를 담게 될 변수
    lambda_k = 0.0
    lambda_k1 = 1.0
    # 위 고유치의 고유 벡터를 저장할 장소
    zk = [1.0] * n

    counter = 0

    while True:
        #행렬 곱셈
        # k 가 큰 값이라면 z_k는 첫번째 고유벡터와 거의 같은 방향이므로
        yk1 = matrix.mul_mat_vec(mat_a, zk)

        lambda_k1 = abs(yk1[0])
        for yk1_i in yk1[1:]:
            if abs(yk1_i) > abs(lambda_k1):
                lambda_k1 = yk1_i

        for i in range(n):
            zk[i] = yk1[i] / lambda_k1
        if abs(lambda_k1 - lambda_k) < epsilon:
            break
        labda_k = lambda_k1

        del yk1
        counter += 1

    if b_verbose:
        print("prower method counter = %d" % counter)

    return lambda_k1, zk

def find_r_s(mat_a0, n):
    r = 0
    s = 1
    ars = mat_a0[r][s]
    abs_ars = abs(ars)

    for i in range(n - 1):
        for j in range(i * 1, n):
            aij = abs(mat_a0[i][j])
            if aij > abs_ars:
                r = i
                s = j
                abs_ars = aij
                ars = mat_a0[i][j]
    return abs_ars, ars, r, s

def calc_theta(ars, arr, ass):
    theta_rad = 0.5 * math.atan2((2.0 * ars), (arr - ass))
    return theta_rad

def jacobi_method(mat_a, epsilon=1e-9, b_verbose=False):
    n = len(mat_a)

    mat_a0 = matrix.alloc_mat(n, n)
    for i in range(n):
        for j in range(n):
            mat_a0[i][j] = mat_a[i][j]

    mat_x = matrix.get_identity_matrix(n)

    while True:
        abs_ars, ars, r, s, = find_r_s(mat_a0, n)

        if abs_ars < epsilon:
            break
        if b_verbose:
            print("ars = %s" % ars)
            print("r, s = %s" % (r, s))

        arr = mat_a0[r][r]
        ass = mat_a0[s][s]

        theta_rad = calc_theta(ars, arr, ass)
        if b_verbose:
            print("theta = %s (deg)" % (theta_rad * 180 / math.pi))
        cos = math.cos(theta_rad)
        sin = math.sin(theta_rad)

        for k in range(n):
            if k == r:
                pass
            elif k == s:
                pass
            else:
                akr = mat_a0[k][r]
                aks = mat_a0[k][s]
                mat_a0[r][k] = akr * cos + aks * sin
                mat_a0[s][k] = aks * cos - akr * sin

                mat_a0[k][r] = mat_a0[r][k]
                mat_a0[k][s] = mat_a0[s][k]

            xkr = mat_x[k][r]
            xks = mat_x[k][s]
            mat_x[k][r] = xkr * cos + xks * sin
            mat_x[k][s] = xks * cos - xkr * sin

        mat_a0[r][r] = arr * cos * cos + 2.0 * ars * sin * cos *ass * sin * sin
        mat_a0[s][s] = arr * sin * sin - 2.0 * ars * sin * cos * ass * cos *cos
        if b_verbose:
            print("mat_a0")
            matrix.show_mat(mat_a0)
            print("mat_x")
            matrix.show_mat(mat_x)

    return mat_a0, mat_x

