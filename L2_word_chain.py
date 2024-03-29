# 해결 전략

# 참가자 들이 말한 단어들을 순서대로 추적하면서, 각 단어가 끝말잇기 규칙을 준수하는지 검사
# 이미 사용된 단어를 저장하기 위한 집합(Set)을 사용하여, 단어가 이전에 사용되었는지 확인
# 각 단어를 말할 때마다, 해당 단어가 이전 단어의 마지막 글자로 시작하는지, 그리고 이전에 사용되지 않았는지 확인
# 위반 사항이 발견되면 즉시 탈락자의 번호와 차례를 계산하여 반환
# 모든 단어가 규칙을 준수하면 [0, 0]을 반환

def solution(n, words):
    used_words = set()  # 사용된 단어를 저장할 집합
    last_char = words[0][0] # 첫 단어의 첫 글자로 시작
    for i, word in enumerate(words):
        # 현재 단어가 이미 사용되었거나, 앞 단어의 마지막 문자로 시작하지 않거나, 한 글자인 단어인 경우 탈락
        if word in used_words or last_char != word[0] or len(word) == 1:
            # 탈락자 번호와 탈락 차례를 반환
            # 사람 번호는 (인덱스 % n) + 1 (사람 번호는 1부터 시작)
            # 탈락 차례는 (인덱스 // n) + 1
            return [(i % n) + 1, (i // n) + 1]
        used_words.add(word)    # 사용된 단어를 집합(set)에 포함
        last_char = word[-1]
    # 모든 단어가 규칙을 준수하면 탈락자가 없음. [0, 0] 반환
    return [0, 0]

# 예시
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))