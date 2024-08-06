# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면,
# 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

def solution(num):
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        cnt += 1
        if cnt > 500:
            return -1
    return cnt

# 다른 사람 풀이
def solution(num):
    cnt = 0
    for i in range(500):
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1

# 예시
n = 6
print(solution(n))  # 8

n = 16
print(solution(n))  # 4

n = 626331
print(solution(n))  # -1