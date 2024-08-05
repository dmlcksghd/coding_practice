# 주어진 계단을 이용하여 최소한의 점프 횟수로 목표 높이 h를 넘는 것이 목표
# 접근 방법 : 최단 경로문제 BFS

from collections import deque


def min_jumps_to_cross(h, n, stairs):
    queue = deque([(0, 0)])  # (현재 위치, 점프 횟수)
    visited = set()  # 방문한 계단 위치
    max_reach = 0  # 현재까지의 최대 도달 높이

    while queue:
        position, jumps = queue.popleft()

        # 목표 높이를 넘었을 때 점프 횟수 반환
        if position > h:
            return jumps

        # 점프 가능한 범위 내의 모든 계단 탐색
        for stair in stairs:
            if position < stair <= position + n and stair not in visited:
                visited.add(stair)
                queue.append((stair, jumps + 1))
                max_reach = max(max_reach, stair)

        # 계단을 이용해 최대 높이까지 도달했을 때 점프 가능
        if max_reach >= position and max_reach + n > h:
            return jumps + 1

    return -1  # 목표를 넘을 수 없는 경우


# 예시 사용
h = 12
n = 3
stairs = [2, 3, 6, 7, 10, 11]
result = min_jumps_to_cross(h, n, stairs)
print(result)  # 예상: 4