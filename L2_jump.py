# 해결 전략
# 이동할 거리 n에 도달하기 전까지 가능한 순간이동을 많이 사용하는 전략

# 구현 방법
# 1. 역으로 거슬러 올라가기(n이 짝수일 경우, 순간이동 사용, n이 홀수일 경우 점프 사용)
# 2. 반복문 또는 재귀 사용
def solution(N):
    battery_usage = 0

    while N > 0:
        # N이 홀수일 경우, 점프를 사용해야 하므로 건전지 사용량 1 증가
        if N % 2 == 1:
            N -= 1
            battery_usage += 1
        # N이 짝수일 경우, 순간이동을 사용 (건전지 사용량 증가 없음)
        else:
            N //= 2

    return battery_usage


# 예시
print(solution(5))  # 2
print(solution(6))  # 2
print(solution(5000))  # 5
