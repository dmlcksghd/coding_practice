# 1. 고유한 종류의 포켓몬 파악
# 2. 최대 선택 가능한 종류 수 결정
# 3. 결정 조건
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    unique_count = len(set(nums))  # 고유한 종류의 포켓몬 수
    max_select = len(nums) // 2  # 선택할 수 있는 최대 포켓몬 수

    # 최대 선택할 수 있는 종류의 수 반환
    return min(unique_count, max_select)