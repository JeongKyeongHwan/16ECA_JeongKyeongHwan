#-*- coding: utf8 -*-
"""
수치 적분 응용 예제
단면의 도심 구하기
"""
import math
import pylab
import num_int

help(num_int.rect0)

def main():

    # 적분 구간 == 단면의 위 끝과 아래 끝
    y_min = 0.0
    y_max = 0.12
    #적분 구간을 나눌 갯수
    n = 120

    # 단면의 면적을 1차 적분으로 구함
    area = num_int.trapezoid1(f, y_min, y_max, n)
    moment_first = num_int.trapezoid1(g, y_min, y_max, n)

    centroid = moment_first / area

    print "area =", area
    print "moment =", moment_first
    print "centroid =", centroid

    y_list = pylab.arange(y_min, y_max, 1e-6)
    w_list = [f(y) for y in y_list]

    # 단면 표시
    pylab.fill_between(y_list, w_list)
    # 도심 위치에 수직선 표시
    pylab.axvline(x=centroid, c="r")

    # 가로축 세로축 비율을 같게 함
    pylab.axis("equal")
    # 모눈 표시
    pylab.grid()

    pylab.show()

def f(y):
    """
    단면의 형상
    H빔 단면과 유사
    대칭인 것으로 가정함
    :param y:
    :return:
    """
    if 0.00 <= y < 0.02:
        r = 0.01
        result = 0.04 + math.sqrt(r * r - (y - r) ** 2)
        # result = 0.06
    elif 0.02 <= y < 0.10:
        result = 0.02
    else:
        result = 0.0

    return result

def g(y):
    result = y * f(y)
    return result

if "__main__" == __name__:
    main()
