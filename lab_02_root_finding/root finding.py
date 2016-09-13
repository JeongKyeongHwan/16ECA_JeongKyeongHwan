#-*- coding: utf8 -*-

'''
1변수 방정식의 해
어떤 (비선형) 함수 f(x)의 값이 0이 되도록 만드는 x를 찾음
'''
# epsilon은 허용되는 오차범위를 의미함
# lxl < epsilon == (x = 0)
# lx - yl < epsilon == (x == y)
epsilon_global = 1e-4

def sequential(f, x0, delta_x=1e-6, epsilon=epsilon_global, b_verbose=False):
    """
    sequential method
    x0로 부터 시작해서 delta_x 만큼씩 증가시키면서 lf(x)l 값이 epsilon값 보다 작아지는지 관찰함
    :param f: f(x) = 0인 x를 찾고자 하는 함수
    :param x0: x의 초기값
    :param delta_x: x를 한번에 delta_x만큼씩 증가시킴
    :param epsilon: 오차 허용 범위
    :param b_verbose: 추가 정보 표시, 정해주지 않으면 False
    :return: lf(x) < epsilon인 x
    """
    xi = float(x0)
    #xi의 초기값은 (부동소숫점) 실수가 되어야 하므로 float()를 이용

    counter = 0

    while Ture:

        fi = f(xi)
        if abs(fi) < epsilon:
            break

        xi += delta_x

        counter += 1

    if b_verbose:

        print "seq_counter=", counter

    return xi

def 