# 로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다. 1

# 순위	당첨 내용
# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외
# 로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
# 알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.

# 당첨 번호	31	10	45	1	6	19	결과
# 최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
# 최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등
# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
# 알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
# 3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
# 알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
# 5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
# 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.


def solution(lottos, win_nums):
    # 0의 개수와 맞춘 번호 개수 세기
    zero_count = lottos.count(0)
    match_count = len(set(lottos) & set(win_nums))

    # 등수를 정하는 함수
    def get_rank(count):
        if count >= 2:
            return 7 - count  # 맞춘 개수에 따라 등수 계산
        else:
            return 6  # 0 ~ 1개 맞춘 경우 6등

    # 최고 순위와 최저 순위 계산
    highest_rank = get_rank(match_count + zero_count)
    lowest_rank = get_rank(match_count)

    return [highest_rank, lowest_rank]

# 개선한 코드
def solution(lottos, win_nums):
    # 0의 개수와 맞춘 번호 개수 세기
    zero_count = lottos.count(0)
    matched = len(set(lottos) & set(win_nums))

    # 순위는 맞춘 개수에 따라 6에ㅔ서 빼는 구조
    highest_rank = min(7 - (matched + zero_count), 6)
    lowest_rank = min(7 - matched, 6)

    return [highest_rank, lowest_rank]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))   # [3, 5]

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))   # [1, 6]

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))   # [1, 1]