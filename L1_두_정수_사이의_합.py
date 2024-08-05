<<<<<<< HEAD
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
=======
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수,
# solution을 완성하세요.
>>>>>>> main

def solution(a, b):
    num = 0
    if a < b:
        for i in range(a, b + 1):
            num += i
        return num
    else:
        for i in range(b, a + 1):
            num += i
        return num
    return a

# 최적화
def solution(a, b):
    # 작은 값과 큰 값을 정해줌
    min_val = min(a, b)
    max_val = max(a, b)

    # 등차수열의 합 공식 : 항의 갯수 * (첫째 항 + 마지막 항) / 2
    return (max_val - min_val + 1) * (min_val + max_val) // 2
