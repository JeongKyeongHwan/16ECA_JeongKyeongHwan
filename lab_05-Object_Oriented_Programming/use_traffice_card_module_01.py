#-*- coding: utf8
"""
교통카드 모듈 사용 예
"""

# 교통카드 모듈을 불러들여 my_card라는 이름과 연결시킴
import traffic_card_module_00 as my_card

help(my_card)

# 불러들인 후 다른 함수를 호출하기 전 잔고를 확인
print("my_card.check() = %s" % my_card.check())
# 10000원 충전. Q: 해당 함수의 반환 값의 의미는?
print("my_card.deposit(10000) = %s" % my_card.deposit(10000))
# 10000원 충전 후 잔고 확인
print("my_card.check() = %s" % my_card.check())
# 버스를 한번 이용하기 위해 지불
print("my_card.pay(1250) = %s" % my_card.pay(1250))
# 잔고 확인
print("my_card.check() = %s" % my_card.check())

# 여러 장의 교통 카드를 만들 수 있나?
# 교통카드 모듈을 불러들여 your_card라는 이름과 연결시킴
import traffic_card_module_00 as your_card

# Q: 잔고 확인 결과 여러 장의 교통카드를 만들 수 있나?
print("your_card.check() = %s" % your_card.check())

# Q: Unit test를 작성해 보시오

