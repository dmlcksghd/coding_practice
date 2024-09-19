from collections import Counter


def solution(k, tangerine):
    # 리스트에 각 귤의 종류마다 카운트 후 내림차순 정렬
    count = Counter(tangerine).most_common()

    # 상자에 넣을 귤의 종류 선택
    total = 0
    result = 0
    for _, c in count:
        total += c
        result += 1
        if total >= k:
            break

    return result


# 예시
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))   # 3

k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))   # 2

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k, tangerine))   # 1

# 시간 복잡도
O(NlogN)