# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            # 타겟 넘버와 일치하는지 확인
            return 1 if current_sum == target else 0

        # 현재 숫자를 더하거나 빼는 두 가지 경우로 재귀 호출
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    return dfs(0, 0)