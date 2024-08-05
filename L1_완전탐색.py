# 수포자는 수학을 포기한 사람의 준말입니다.
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
#
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
#
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    # 수포자의 패턴을 정의
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    # 각 수포자의 점수
    scores = [0, 0, 0]

    # 정답과 수포자 패턴 비교
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == patterns[j][i % len(patterns[j])]:
                scores[j] += 1

    # 최대 점수 계산
    max_score = max(scores)

    # 결과 반환
    answer = []
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)    # 수포자는 1번부터 시작해서 3번까지 있음

    return answer

# 예제 입력
answers = [1, 2, 3, 4, 5]
print(solution(answers))    # [1]

answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

print(solution(answers))    # [3]