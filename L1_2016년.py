# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.


def solution(a, b):
    total_days = 0  # 총 일 수
    month_dict = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    day_dict = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    # 이전 달까지의 총 일수를 계산
    for month in range(1, a):
        total_days += month_dict[month]

    # 현재 달의 일수(b)도 더한 후, 요일 계산
    total_days += b - 1
    return day_dict[total_days % 7]

# 예제
a = 5
b = 24
print(solution(a, b))   # TUE