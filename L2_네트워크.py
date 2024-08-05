# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    def dfs(node):  # 입력 매개변수 node : 현재 방문하려는 컴퓨터(노드)의 번호
        # visited 배열을 초기화하여 모든 컴퓨터가 방문되지 않은 상태로 시작
        visited[node] = True    # 현재 노드를 방문 했음
        for i in range(n):  # 현재 노드와 연결된 다른 컴퓨터들을 찾음
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)

        visited = [False] * n
        network_count = 0

    for i in ragne(n):
        if not visited[i]:
            dfs(i)
            network_count += 1

    return network_count
