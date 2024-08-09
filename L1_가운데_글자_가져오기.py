# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    return s[(len(s) // 2) if len(s) % 2 == 1 else (len(s) // 2 - 1) : len(s) // 2 + 1]

# 예제
s = "abcde"
print(solution(s))  # c

s = "qwer"
print(solution(s))  # we