# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

def solution(s):
    # 숫자와 영단어 매핑을 위한 딕셔너리
    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

    # 딕셔너리를 사용하여 영단어를 숫자로 치환
    for word, num in num_dict.items():
        s = s.replace(word, num)

    # 최종적으로 숫자 문자열을 정수로 변환
    return int(s)

# 다른 사람 풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        # 인덱스를 활용하여 숫자를 str로 변환
        s = s.replace(words[i], str(i))

    return int(s)

# 예시
s = "one4seveneight"
print(solution(s))  # 1478

s = "23four5six7"
print(solution(s))  # 234567

s = "2three45sixseven"
print(solution(s))  # 234567

s = "123"
print(solution(s))  # 123


