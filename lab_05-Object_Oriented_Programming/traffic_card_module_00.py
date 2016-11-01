#-*- coding: utf8
"""
교통가드 모듈
잔고는 모듈 전역변수 balance_won에 저장됨
"""

# balance_won은 교통카드 잔고를 기억시킬 전역 변수. 이 .py 파이 안 어디에서나 사용할 수 있음

balance_won = 0

def deposit(amount):
    """
    교통카드에 입금
    :param amount: int
    :return:
    """
    # 전역변수 balance_won 사용을 명시함
    global balance_won
    #balace_won 을 amount 만큼 증가시킴
    # Q: amount 가 0보다 작다면?
    balance_won += int(amount)

def pay(amount):
    """
    교통카드로 지불
    :param amount:int
    :return:
    """
    # 전역변수 balance_won 사용을 명시함
    global balance_won
    # balance_won 을 amount 만큼 감소시킴
    # Q: amount 가 0보다 작다면?
    balance_won -= int(amount)

def check():
    """
    잔고 확인
    :return: int
    """
    # 전역변수 balance_won 사용을 명시함
    # check()함수를 사용하지 않고 잔액을 확일할 수 있는가?
    # 확일할 수 있는 쪽과 없는 쪽 어느 쪽이 더 바람직 한가?
    global balance_won
    return balance_won


