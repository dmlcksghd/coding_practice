# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 유클리드 호제법 : 두 수 a, b (a > b)에 대해, a를 b로 나눈 나머지를 r이라 할 때, GCD(a, b) = GCD(b, r)입니다. 이 과정을 반복하여 나머지가 0이 될 때 나누는 수가 최대 공약수
# 최소 공배수(LCM) : GCD(8, 12) = 4이고, LCM(8, 12) = (8 * 12) / 4 = 24
def solution(n, m):
    max_num = max(n, m)
    min_num = min(n, m)

    while min_num != 0:
        remainder = max_num % min_num
        max_num = min_num
        min_num = remainder

    gcd = max_num
    lcm = (n * m) // gcd
    return [gcd, lcm]

# 예제
n = 3
m = 12
print(solution(n, m))

n = 2
m = 5
print(solution(n, m))