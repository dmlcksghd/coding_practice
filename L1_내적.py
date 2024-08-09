# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다.
#  a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

# 다른사람 풀이
def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])

# 예제
a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a, b))   # 3

a = [-1,0,1]
b = [1,0,-1]
print(solution(a, b))   # -2