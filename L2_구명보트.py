# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.


# 큐를 활용
from collections import deque


def solution(people, limit):
    people.sort()  # 몸무게 오름차순 정렬
    people = deque(people)  # 큐로 변환
    boats = 0

    while people:
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.popleft()  # 가장 가벼운 사람 제거
            people.pop()  # 가장 무거운 사람 제거
        else:
            people.pop()
        boats += 1
    return boats


# 다른풀이(탐욕법)
def solution(people, limit):
    # 사람들의 몸무게 정렬
    people.sort()

    left = 0  # 가장 가벼운 사람을 가리키는 포인터
    right = len(people) - 1
    boats = 0

    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 무게 합이 limit을 초과하지 않으면
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats


# 예시
people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))  # 3

people = [70, 80, 50]
limit = 100
print(solution(people, limit))  # 3

# 시간복잡도
# 1. O(NlogN)   정렬(NlogN) + while(N)
# 2. O(NlogN)