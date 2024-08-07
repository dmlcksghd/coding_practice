# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

def solution(seoul):
    for index, ch in enumerate(seoul):
        if ch == 'Kim':
            answer = f"김서방은 {index}에 있다"
            return answer

# 예시
seoul = ["Jane", "Kim"]
print(solution(seoul))

# 다른 사람 풀이
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 예시
seoul = ["Jane", "Kim"]
print(solution(seoul))