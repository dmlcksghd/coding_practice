# "명예의 전당"이라는 TV 프로그램에서는 매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다. 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다. 즉 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다. k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.

# 이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표합니다. 예를 들어, k = 3이고, 7일 동안 진행된 가수의 점수가 [10, 100, 20, 150, 1, 100, 200]이라면, 명예의 전당에서 발표된 점수는 아래의 그림과 같이 [10, 10, 10, 20, 20, 100, 100]입니다.

# 명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때, 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.
def solution(k, score):
    answer = []
    rank = []

    for i in score:
        if len(rank) < k:
            rank.append(i)
        else:
            if i > min(rank):
                rank.remove(min(rank))
                rank.append(i)

        # 현재 명예의 전당에서 가장 낮은 점수 기록
        answer.append(min(rank))

    # 매일 새로운 점수가 들어오면, 현재 명예의 전당 목록과 비교

    return answer


# 힙을 사용한 풀이, heapq는 최소힙임. 최대 힙 사용하고 싶으면 입력할때 음수(-)값으로 입력하고 출력할때 음수(-)값 붙여서 출력하면됨
def solution(k, score):
    import heapq
    rank = []
    answer = []

    for i in score:
        # 힙에 새로운 점수 추가
        heapq.heappush(rank, i)

        # 힙의 크기가 k를 넘으면 최솟값을 제거
        if len(rank) > k:
            heapq.heappop(rank)

        # 힙에서 가장 작은 값이 명예의 전당 최하위 점수
        answer.append(rank[0])

    return answer


# 예시 1
k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))  # 출력: [10, 10, 10, 20, 20, 100, 100]

# 예시 2
k = 4
score = [10, 30, 40, 3, 20, 50]
print(solution(k, score))  # 출력: [10, 10, 10, 10, 20, 30]
