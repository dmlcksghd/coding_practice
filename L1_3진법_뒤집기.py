# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
def solution(n):
    stack = []

    # n이 0이 될 때까지 3으로 나눈 나머지를 스택에 추가
    while n > 0:
        stack.append(n % 3)
        n //= 3

    # 3진법으로 표현된 숫자를 10진법으로 변환
    answer = 0
    for i in range(len(stack)):
        answer += stack.pop() * (3 ** i)

    return answer

# 다른 사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)    # 8진법 변환은 oct, 16진법 변환은 hex 사용
    return answer


# 예제
n = 45
print(solution(n))  # 7

n = 125
print(solution(n))  # 229