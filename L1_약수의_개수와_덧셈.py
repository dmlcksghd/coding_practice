# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
def find_divisor(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if len(find_divisor(i)) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

# 코드 최적화
# 완전 제곱수 int(i**0.5) == i**0.5 가 성립되면 약수의 개수는 홀수
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i

    return answer

# 예제
left = 13
right = 17
print(solution(left, right))

left = 24
right = 27
print(solution(left, right))
