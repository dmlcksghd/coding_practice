# 숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.

# 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.

# 예를 들어, 15번으로 지정된 기사단원은 15의 약수가 1, 3, 5, 15로 4개 이므로, 공격력이 4인 무기를 구매합니다. 만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면, 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.

# 기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.


def count_divisors(n):
    # n의 약수 개수를 계산하는 함수
    count = 0

    # 1부터 n의 제곱근까지 반복
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # i가 n의 약수라면 약수 개수에 추가
            count += 1
            # i와 n // i 가 서로 다른 경우, n // i도 약수로 추가
            if i != n // i:
                count += 1
    return count


def solution(number, limit, power):
    #  필요한 철의 총 무게를 저장할 변수
    total_weight = 0

    # 1부터 number까지의 각 기사 번호에 대해 반복
    for num in range(1, number + 1):
        # 현재 기사 번호의 약수 개수 계산
        divisors_count = count_divisors(num)
        # 약수 개수가 limit을 초과하면 power를 추가
        if divisors_count > limit:
            total_weight += power
        # 약수 개수가 limit 이하이면 약수 개수를 추가
        else:
            total_weight += divisors_count

    return total_weight


# 예시
number = 5
limit = 3
power = 2
print(solution(number, limit, power))   # 10

number = 10
limit = 3
power = 2
print(solution(number, limit, power))   # 21