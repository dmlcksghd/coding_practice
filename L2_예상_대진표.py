def solution(n, a, b):
    round = 0

    # A와 B가 만날 때 까지 계속 반복
    while a != b:
        # 번호 갱신
        a = (a + 1) // 2
        b = (b + 1) // 2
        # 라운드 카운트 증가
        round += 1

    return round

# 예시

n = 8
a = 4
b = 7
print(solution(n, a, b))    # 3

# 시간 복잡도
O(logN)