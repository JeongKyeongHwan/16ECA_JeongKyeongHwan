#-*- coding: utf8 -*-

import matplotlib.pyplot as plt

plt.rcdefaults()
# rc관련 설정을 초기화 해 줌

import numpy as np
# 배열, 행렬 관련 기능을 담고 있는 numpy 모듈을 불러 들임

people = ('Tom', "Dick", 'harry', "slim", 'Jim')

y_pos = np.arange(len(people))
# 사람 이름의 축 위의 순서

performance = 3 + 10 * np.random.rand(len(people))
# 성능 (한사람에 하나씩 임의의 숫자)

error = np.random.rand(len(people))
# 오차 (한사람에 하나씩 임의의 숫자)

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
# 가로 막대 그래프 생성

plt.yticks(y_pos, people)
# y 축을 따라 사람 이름을 표시

plt.xlabel('Performance')
# x 축 이름

plt.title('How fast do you want to go today?')
# 그래프 제목

plt.show()
