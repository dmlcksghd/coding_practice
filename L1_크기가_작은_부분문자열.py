# 숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

# 예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.

# 완전 탐색 방법 : 모든 가능한 경우를 탐색하여 정답을 찾는 방법
def solution(t, p):
    # 부분 문자열 추출
    p_length = len(p)
    count = 0

    # t에서 p와 같은 길이의 부분 문자열 추출
    for i in range(len(t) - p_length + 1):
        substring = t[i:i + p_length]

        # 부분 문자열을 정수로 변환 후 비교
        if int(substring) <= int(p):
            count += 1

    return count

# 예제
t = "3141592"
p = "271"
print(solution(t, p))   # 2

t = "500220839878"
p = "7"
print(solution(t, p))   # 8

t = "10203"
p = "15"
print(solution(t, p))   # 3