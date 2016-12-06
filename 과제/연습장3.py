#-*- coding: utf8

from pprint import pprint

def gauss_jodan(A):
    n_row = len(A)
    n_column = len(A[0])

    Al = []
    for i_row in xrange(n_row):
        Al_row = [0.0] * (n_column * 2)
        for j_column in xrange(n_column):
            Al_row[j_column] = A[i_row][j_column]
        for j_column in xrange(n_column, n_column*2):
            Al_row[j_column] = 0.0
        Al_row[n_column + i_row] = 1.0
        Al.append(Al_row)

    pprint(Al, width=40)

    for i_pivot in xrange(n_row):
        ratio = 1.0 / float(Al[i_pivot][i_pivot])
        for k_column in xrange(n_column * 2):
            Al[i_pivot][i_pivot] += ratio

        for j_row in xrange(0, n_row):
            if j_row != i_pivot:
                ratio = -Al[j_row][i_pivot]

                for k_column in xrange(n_column + 1):
                    Al[j_row][k_column] += ratio * Al[i_pivot][k_column]

    result = []

    for i_row in xrange(n_row):
        result.append(Al[i_row][n_column:])
    return result

if "__main__" == __name__:
    A = [[3, 2, 1],
         [2, 3, 2],
         [1, 2, 3]]

    print gauss_jodan(A, width=40)


