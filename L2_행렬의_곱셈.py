def solution(arr1, arr2):
    # arr1의 행(row) 개수와 arr2의 열(column) 개수를 구합니다.
    n = len(arr1)
    m = len(arr2[0])
    k = len(arr2)

    # 결과 행렬을 0으로 초기화
    result = [[0] * m for _ in range(n)]

    # 행렬 곱셈 수행
    for i in range(n):  # arr1의 행
        for j in range(m):  # arr2의 열
            for x in range(k):  # arr1의 열과 arr2의 행
                result[i][j] += arr1[i][x] * arr2[x][j]

    return result

# 예시
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2)) # [[15, 15], [15, 15], [15, 15]]