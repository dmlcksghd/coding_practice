# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        return [-1]
    return sorted(answer)

# 예시
arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))   # [5, 10]

arr = [3, 2, 6]
divisor = 10
print(solution(arr, divisor))   # [-1]