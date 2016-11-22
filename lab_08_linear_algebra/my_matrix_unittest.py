#-*- coding: utf8

'''
행렬 간련 모듈을 위한 unit test class
mat_로 시작하는 instance 변수들을 행렬로 가정하고 각 test 후 삭제

'''

import itertools

import my_unittest
from my_unittest import main

class MyMatrixTestCase(my_unittest.MyTestCase):
    def assertMarixAlmostEqual(self, mat1, mat2, msg=None, places=None, delta=None):
        # row size check
        self.assertEqual(len(mat1), len(mat2), msg="len(mat1) != len(mat2)")

        # sheck each row

        for row1, row2 in itertools.izip(mat1, mat2):
            self.assertSequenceAlmostEqual(row1, row2, msg=msg, places=places, delta=delta)

        def tearDown(self):
            # iterate over object attributes in python.
            # http://stackoverflow.com/questions/11637293/itertae-over-object-attributes-in-python
            for key in dir(self):
                attr = getattr(self, key)
                if key.startswith('mat...'):
                    del attr[:]

