# W * H = brown + yellow
# brown = W * H - yellow
# (W -2) + (H - 2) = yellow
# brown = 2W + 2H -4

def solution(brown, yellow):
    # 전체 카펫의 격자 수는 brown과 yellow 격자의 합
    total = brown + yellow

    for H in range(1, total + 1):
        # H가 전체 격자 수를 나눌 수 있는 지 확인
        if total % H == 0:
            W = total // H
        if (W - 2) * (H - 2) == yellow:
            return [W, H]


brown = 10
yellow = 2
print(solution(brown, yellow))