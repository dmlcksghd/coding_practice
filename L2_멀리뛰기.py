# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.


from itertools import combinations


def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # 피보나치 계산을 위한 초기 값
    prev1 = 1
    prev2 = 2

    for i in range(3, n + 1):
        curr = (prev1 + prev2) % 1234567
        prev1 = prev2
        prev2 = curr

    return prev2


# 예시
n = 4
print(solution(n))  # 5

n = 3
print(solution(n))  # 3

# 시간복잡도
# O(N) -> 피보나치 수열은 f(n) = f(n-1) + f(n-2)

