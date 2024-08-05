# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    all_numbers = set()  # 중복을 피하기 위해 집합 사용
    # 모든 자리수의 순열 생성
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))  # 순열을 정수로 변환
            all_numbers.add(num)  # 집합에 추가하여 중복 제거

    prime_count = 0
    # 집합에 저장된 모든 숫자에 대해 소수 판별
    for num in all_numbers:
        if is_prime(num):
            prime_count += 1

    return prime_count
