# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

import re

def solution(phone_number):
    return re.sub(r'\d', '*', phone_number[:-4]) + phone_number[-4:]

def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]

# ljust, rjust(채울 길이, 뭘로채울건지) 사용하여 번호 채우기
def solution(phone_number):
    return phone_number[-4:].rjust(len(phone_number), '*')

# 예제
phone_number = "01033334444"    # "*******4444"
print(solution(phone_number))