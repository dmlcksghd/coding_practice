# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.
def solution(price, money, count):
    total_price, cnt = 0, 0
    for cnt in range(1, count + 1):
        total_price += price * cnt
    return total_price - money if total_price - money > 0 else 0

# 최적화
# 등차수열의 합 : (항의 개수 * (첫번째항 + 마지막 항)) // 2
def solution(price, money, count):
    total_price = count * (price + (price * count)) // 2

    return max(0, total_price - money)


# 예제
price = 3
money = 20
count = 4
print(solution(price, money, count))