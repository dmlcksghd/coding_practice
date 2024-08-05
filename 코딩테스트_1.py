# n,m,point가 주어지고 nxm으로 이루어진 사각형에 주어진 포인트배열이 주어져서 특정위치를 비운다고하면 남은 철사가 이어진 부분이 몇개 존재하는지 찾는문제
# 연결요소 찾기 DFS 이용
def count_connected_components(n, m, points):
    # 격자 초기화
    grid = [[1] * m for _ in range(n)] # [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    # 구멍 좌표
    for x, y in points:
        #print(f"(x,y): ({x},{y})")
        grid[x][y] = 0

    # DFS를 이용한 연결 요소 찾기
    def dfs(x, y):
        # 격자 범위를 벗어나거나 철사가 없는 곳이면 종료
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return
        # 방문한곳은 0으로 표시
        grid[x][y] = 0
        # 상, 하, 좌, 우 탐색
        dfs(x + 1, y)   # 하
        dfs(x - 1, y)   # 상
        dfs(x, y + 1)   # 우
        dfs(x, y - 1)   # 좌

    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j)
                cnt += 1

    return cnt

# 예시 사용
n = 4
m = 3
points = [(0, 2), (1, 2), (2, 2)]   # 예시 구멍 좌표
results = count_connected_components(n, m, points)
print(results)