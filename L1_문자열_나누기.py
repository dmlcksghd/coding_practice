# 카운팅 로직, 반복문
def solution(s):
    count = 0
    i = 0

    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0

        # 문자열을 순차적으로 탐색하며 x와 다른 글자의 횟수 카운트
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1

            i += 1

            # 두 횟수가 같아지는 순간 문자열을 분리합니다.
            if x_count == other_count:
                break

        # 분리된 문자열이 하나 추가됨
        count += 1

    return count


# 다른 풀이
def solution(s):
    count = 0
    balance = 0

    for word in s:
        if balance == 0:
            count += 1
            x = word

        if word == x:
            balance += 1
        else:
            balance -= 1

    return count

#  예시
s = "banana"
print(solution(s))  # 3

s = "abracadabra"
print(solution(s))  # 6

s = "aaabbaccccabba"
print(solution(s))  # 3