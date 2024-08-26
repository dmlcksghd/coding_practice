# 문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.
#
# 먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
# 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
# s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
# 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
# 문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.


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