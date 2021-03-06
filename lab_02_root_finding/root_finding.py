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

    while True:

        fi = f(xi)
        if abs(fi) < epsilon:
            break

        xi += delta_x

        counter += 1

    if b_verbose:

        print "seq_counter=", counter

    return xi
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

    if b_verbose:
        # counter를 표시
        print "bis_counter =", counter

    # xn을 반환
    return xn
#end of biosection()


def newton(f, df, x0, epsilon=epsilon_global, b_verbose=False):
    """
    Newton Raphson method
    비선형 함수이 f(x)의 xi 지점에서의 접선의 방정식의 근을 구함

    xi 지점에서의 f(x)의 기울기가 di, 함수값이 fi 이면
    접선의 방정식 di (x - xi) + fi 는 x = xi - fi/di 이면 0이 됨
    즉, 접선의 방정식의 근을 xi - fi/di 이고 접점 xi로부터 (-fi/di) 위치에 있음
    이를 이용하여 i + 1 번째 x를 xi - fi/di로 정함

    f(x)의 xi에서의 기울기 di의 절대값이 0에 가까울 경우 xi로 부터 매우 먼 위치에 xi가 자리하게 됨
    새로운 위치에서 lf(x)l 값이 epsilon 값 보다 작아지면 중단
    그렇지 않으면 접선의 방정식의 근을 다시 구함

    :param f: f(x) = 0을 만족하는 x를 찾고자 하는 함수
    :param df: f(x)의 미분
    :param x0: x의 초기값
    :param epsilo: 오차 허용 한도도
    :paramb_verbose: 추가 정보 표시, 정해주지 않으면 False
    :return: lf(x) < epsilon인 x
    """
    xi = float(x0)
    # xi를 부동소숫점 실수로 초기화

    counter = 0

    while True:
        fi = f(xi)

        counter += 1

        if abs(fi) < epsilon:
            break

        else:
            xi += (-fi / df(xi))

    if b_verbose:
        print("nr_counter = %d" % counter)

    return xi

def func(x):
    """
    f(x) =  0을 만족하는 x를 찾고자 하는 f()
    이 경우는 x + x - 2.0 = 0 을 만족하는 x를 찾게 되며 이러한 x는 2 ** 0.5 즉 2의 제곱근임
    :param x:
    :return:
    """

    return 1.0 * x * x - 2.0

def dfunc(x):
    """
    위 함수 func(x)를 x로 미분한 함수
    :param x:
    :return:
    """
    return 2.0 * x

def main():
    # 순차 대입법 sequential method로 Func()의 해를 구하기 위해 시도
    x0 = "0.01"
    x_seq = sequential(func, x0, b_verbose=True)
    print "x_seq =", x_seq
    print "f(x_seq) =", func(x_seq)

    x_bis = bisection(func, 0.01, 2.0, b_verbose=True)
    print 'x_bis=', x_bis
    print "f(x_bis) =", func(x_bis)

    x_nr = newton(func, dfunc, 2.0, b_verbose=True)
    print 'x_nr =', x_nr
    print "f(x_nr) =", func(x_nr)
    # 뉴튼-랩슨법 Newton Raphson method로 func()의 해를 구하기 위해 시도
    # 위의 두 방법에서는 필요하지 않았던 매개변수는?, 초기값은 얼마인가?

    print "error    seq        biss        nr"
    print "        %7g %7g %7g" % ((abs(2.0 ** 0.5 - x_seq)), abs(2.0 ** 0.5 - x_bis), abs(2.0 ** 0.5 - x_nr))


if "__main__" == __name__:
    main()


