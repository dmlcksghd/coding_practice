# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))

    return answer

# 딕셔너리를 이용한 정렬
def solution(strings, n):
    string_dict = {}

    for string in strings:
        string_dict[string] = ord(string[n])

    # 정렬 : string_dict의 값을 기준으로, 값이 같다면 사전순으로 정렬
    answer = sorted(string_dict.keys(), key=lambda x: (string_dict[x], x))

    return answer

# 예제 실행
strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n)) # ['car', 'bed', 'sun']

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n)) # ['abcd', 'abce', 'cdx']