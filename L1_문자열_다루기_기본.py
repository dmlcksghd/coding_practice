# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False

# 예외처리로 작성해봄
def solution(s):
    try:
        # s를 정수로 변환 시도
        int(s)
        # 변환 성공 시 길이 확인
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    except ValueError:
            # 변환 실패 : s가 숫자가 아닌 문자를 포함
        return False


# 예제
s = "a234"
print(solution(s)):

s = "1234"
print(solution(s)):