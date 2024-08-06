
def solution(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

# 예시
n = 12  # 28
print(solution(n))

n = 28
print(solution(n))  # 56