# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    comb_list = []
    count = 0

    for ch in babbling:
        for word in words:
            # 연속된 발음이 있으면 건너뜀
            if word * 2 in ch:
                break
            # 발음할 수 있는 단어를 공백으로 대체
            ch = ch.replace(word, ' ')

        # 공백을 모두 제거한 후 길이가 0이면 발음 가능
        if ch.strip() == '':
            count += 1

    return count


# 예시
babbling =["aya", "yee", "u", "maa"]
print(solution(babbling))   # 1

babbling =["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))   # 2