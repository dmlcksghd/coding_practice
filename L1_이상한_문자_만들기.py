# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
def solution(s):
    words = s.split(' ')  # 공백을 기준으로 단어 분리
    answer = []

    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:  # 짝수 인덱스
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer.append(new_word)

    return ' '.join(answer)

# 예제
s = "try hello world"
print(solution(s))