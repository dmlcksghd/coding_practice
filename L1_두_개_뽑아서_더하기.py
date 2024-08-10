# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 조합(combination) 사용
def solution(numbers):
    from itertools import combinations
    answer = []

    # 조합의 합계를 answer 리스트에 추가
    for num in combinations(numbers, 2):
        answer.append(sum(num))

    # 중복 제거
    answer = list(set(answer))

    # 정렬
    answer.sort()

    return answer

# 예제
numbers = [2,1,3,4,1]
print(solution(numbers))

numbers = [5,0,2,7]
print(solution(numbers))
