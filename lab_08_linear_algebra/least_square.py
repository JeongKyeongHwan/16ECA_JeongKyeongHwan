#-*- coding: utf8

import random

import pylab

import gauss_jordan as gj
import matrix as matrix

random.seed()

def least_square_first_order(vec_x, vec_y):
    """
    x 와 y사이에
    y = ax + b
    와 같은 관계가 있을 것을 가정하고 a, b를 찾으려고 함

    :param vec_x: List[float]
    :param vec_y: List[float]
    :return:
    """
    # 예를 들어 deta point의 갯수를 n 이라 할 때
    mat_x_t = [vec_x,
               [1] * len(vec_x)] # Q 이 행렬의 크기는?
    mat_x = matrix.transpose_mat(mat_x_t) # Q 이 행렬의 크기는?
    mat_v_measured = matrix.transpose_mat([vec_y])
    mat_w_estimated = mul_left_inverse(mat_x, mat_v_measured)

    return mat_w_estimated

def mul_left_inverse(mat_x, mat_y):
    """
    행렬
    :param mat_x:
    :param mat_y:
    :return:
    """
    # 예를 들어 deta point의 갯수를n,
    # 매개변수의 갯수를 n이라 할때
    mat_x_t = matrix.transpose_mat(mat_x)
    mat_xt_x = matrix.mul_mat(mat_x_t, mat_x)
    mat_xt_x_inv = gj.gauss_jordan(mat_xt_x)
    mat_x_left_inverse = matrix.mul_mat(mat_xt_x_inv, mat_x_t)

    return mat_x_left_inverse

def contaminate(vec_y, standard_deviation=0.5):
    vec_y_measured = [yi + random.gauss(0.0, standard_deviation) for yi in vec_y]
    return vec_y_measured

def visualize_least_square_first_order(a_hat, b_hat, vec_x, vec_y, vec_y_measured):
    pylab.plot(vec_x, [a_hat * xi + b_hat for xi in vec_x], label='estimated')
    pylab.plot(vec_x, vec_y_measured, '.', label='measured')
    pylab.plot(vec_x, vec_y, 'r', label='truth')
    pylab.grid(True)
    pylab.legend(loc=0)
    pylab.show()

