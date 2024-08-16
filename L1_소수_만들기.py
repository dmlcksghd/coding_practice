# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


from itertools import combinations
def is_prime(n):
    if n < 2:
        return False
    # 에라토스테네스의 체 방법으로 소수 계산
    for prime in range(2, int(n ** 0.5) + 1):
        if n % prime == 0:
            return False
    return True


def solution(nums):
    count = 0
    # 주어진 숫자 중 3개의 조합 생성
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)): # 생성한 조합을 더해서 소수 판별 함수로 판별
            count += 1

    return count


# 예제
nums = [1,2,3,4]
print(solution(nums))   # 1

nums = [1,2,7,6,4]
print(solution(nums))   # 4