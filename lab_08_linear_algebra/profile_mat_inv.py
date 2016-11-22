#-*- coding: utf8

'''
역행렬 함수 성능 조사 프로그램
딸림 행렬과 Gauss Jordan법의 연산 시간을 비교
cProfile, patats모듈 사용
'''

import os

import gauss_jordan as gj
import matrix

def main():
    import sys

    filename_profile = 'cProfle.result'
    if 2 <= len(sys.argv):
        if 'run' == sys.argv[1]:
            profile(filename_profile)
        elif 'read' == sys.argv[1]:
            if os.path.exists(filename_profile):
                read_profile_result(filename_profile)
            else:
                print('Cannot find result file %s' % filename_profile)
        else:
            print('please choose "read" or "run"')
    else:
        print('please choose "read" or "run"')

def profile(filename_profile):
    import cProfile

    cProfile.run('run_mat_inv()', filename_profile)
    read_profile_result(filename_profile)

def read_profile_result(filename_profile):
    import pstats
    p = pstats.Stats(filename_profile)

    p.strip_dirs()
    p.sort_stats('cumulative', 'time')
    p.print_stats(50)

def run_matj_inv():
    n = 2
    mat_a = matrix.get_random_mat(n, n)
    mat_a_adj = matrix.abjugate_matrix(mat_a)
    mat_a_gj = gj.gauss_jordan(mat_a)

if __name__ == '__main__':
    main()

