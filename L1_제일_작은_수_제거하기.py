def solution(arr):
    arr.remove(min(arr))  # 가장 작은 요소 제거
    if not arr:
        return [-1]
    return arr

# 예시
arr = [10, 3, 5, 2, 1]  # [10, 3, 5, 2]
print(solution(arr))