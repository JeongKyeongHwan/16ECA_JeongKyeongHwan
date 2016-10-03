#-*- coding: utf8 -*-

'''
1변수 방정식의 해
어떤 (비선형) 함수 f(x)의 값이 0이 되도록 만드는 x를 찾음
'''
# epsilon은 허용되는 오차범위를 의미함
# lxl < epsilon == (x = 0)
# lx - yl < epsilon == (x == y)
epsilon_global = 1e-4

def bisection(f, xl, xh, epsilon=epsilon_global, b_verbose=False):
    """
    bisection method
    f(xl)과 f(xh)의 부호가 반대인 xl, xh 에서 시작
    xl ~ xh 사이의 구간의 절반 지점인 xn을 찾음
    f(xl)과 f(xn)의 부호가 반대이면 xh를 xn으로 옮김
    이렇게 하면 계속 f(xl)과 f(xh)의 부호가 반대임
    그렇지 않으면 xl을 xn으로 옮김

    xl ~ xh 사이의 구간의 길이가 eqsilon 보다 작아지면 중단

    :param f: f(x) = 0 인 x를 찾고자 하는 함수
    :param xl: x의 초기값 xl < xh && f(xl) f(xh) < 0
    :param xh: x의 초기값 xl < xh && f(xl) f(xh) < 0
    :param epsilon: 오차 허용 범위
    :param b_verbose: 중간 과정 표시. 정해 주지 않으면 False
    :return: f(x) == 0 인 x 와 가까운 값
    """

    # 어떤 형태의 입력값이 들어올지 알 수 없으나
    # xi의 초기값은 (부동소숫점) 실수가 되어야 하므로
    # float()를 이용
    xl = float(xl)
    xh = float(xh)

    # xn을 초기화 한다
    xn = xl
    # counter는 아래 무한 반복문을 실행한 횟수
    counter = 0

    #무한 반복문
    while True:
        # xl ~ xh 사이의 가운데 지점을 xn으로 삼는다
        xn = 0.5 * (xl + xh)

        # t(xn)과 f(xh)이 부호를 비교
        if f(xn) * f(xh) < 0:
            # 다르면 : 근이 xh - xh 사이에 있음 xl에 xn을 저장
            xl = xn
        else:
            #같으면 : 근이 xl ~ xn 사이에 있음 xh에 xn을 저장
            xh = xn
        # 반복문이 한번 실행 되었으므로 xounter를 1 증가 시킴

        if b_verbose:
            #중간 과정을 표시
            print ('xl = %8f f(xl) = %+8f  xh = %+8f f(xn) = %+8f wh = %+8f f(xh) = %8f Ixh-xlI = %-8f' % (xl, f(xl), xn, f(xn), xh, f(xh), abs(xh - xl)))

        # xl ~ xh 구간의 길이가 epsilon 보다 짧으면 무한 반복문을 중단
        if abs(xh - xl) < epsilon:
            break

    # xn을 반환
    return xn
#end of biosection()


def func(x):

    return 10 * 101.33 / 9.8 - x


def main():

    x_bis = bisection(func, 0, 206, b_verbose=True)
    print 'x_bis=', x_bis
    print "f(x_bis) =", func(x_bis)

if "__main__" == __name__:
    main()


