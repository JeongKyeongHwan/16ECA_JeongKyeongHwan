#-*- coding: utf8 -*-

def rect0(f, xi, xe, n=100):
    """
    0차 수치 적분
    xi ~xe 사이를 n 개의 구획으로 나눔
    한귀획 안에서는 f(x)가 상수일 것이라고 가정함
    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구획을 나누는 갯수
    :return: f(x)를 xi ~xe 구간에서 정적분한 근사값
    """
    # n개로 나눈 각 구획의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 각 구획 중간지점 x 값의 list를 만듦
    # k = 0, 1, 2 ... , (n-1)
    x = [xi + delta_x * (0.5 + k) for k in xrange(n)]

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0

    # 주 반복문 main loop
    # 각 구획별로 연산을 반복 실시
    # k = 0, 1, 2 ..., (n-1)
    for k in xrange(n):
        # k 번째 x 값을 위에서 만든 list 에서 찾음
        xk = x[k]
        # k 번째 귀획의 넓이를 직사각형의 면적으로 구함
        area_k = f(xk) * delta_x
        # 적분 결과에 누적시킴
        result += area_k
    #주 반복문 끝

    #적분 결과를 반환함
    return result

def trapezoid1(f, xi, xe, n=100):
    """
    1차 수치 적분
    xi ~ xe 사이를 n개의 구획으로 나눔
    한 구획 안에서는 f(x)가 1차 직선일 것이라고 가정함
    :param f: 적분될 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝 지점
    :param n: 구간을 나누는 갯수
    :return: f(x)를 xi ~ xe 구간에서 정적분한 근사값
    """

    # n 개로 나눈 각 구획의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 적분 구획 시작 지점 k 번째 x 초기화
    xk = xi
    # 적분 구획 시작 지점 함수값 k번째 f(x)초기화
    fxk = f(xk)

    # 적분 결과를 저장할 변수를 초기화
    result = 0.0

    # 주 반복문 main loop
    # 각 구획별로 연산을 반복 실시
    # k = 1~n-1까지
    for k in xrange(n):
        # 적분 구획 끈 지점 k+1 번째 x 계산
        xk1 = xk + delta_x
        # 적분 구획 끝 지점 k+1 번째 f(x) 계산
        fxk1 = f(xk1)
        # k 번재 구획의 면적을 사다리꼴 공식으로 계산
        area_k = (fxk + fxk1) * delta_x * 0.5
        # 적분 결과에 누적시킴
        result += area_k

        # 현재 구획의 끝점이 다음 구획의 시작점이 됨
        # k+1 번째 x 값을 다음 구획 시작점의 x 값으로 지정
        xk = xk1
        # k+1 번째 f(x) 값을 다음 구획 시작점의 f(x) 값으로 지정
        fxk = fxk1
    # 주 반복문 끝

    #적분 결과를 반환함
    return result


def f(x):
    return 2 * 0.0728 / 9.789 / (x)

def main():

    x_begin = 0.5
    x_end = 2.0
    n_interval = 16

    integraction_0 = rect0(f, x_begin, x_end, n_interval)
    print "integration_0 =", integraction_0

    integraction_1 = trapezoid1(f, x_begin, x_end, n_interval)
    print "integration_1 =", integraction_1

if "__main__" == __name__:
    main()