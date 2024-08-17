def solution(dartResult):
    stack = []
    i = 0
    length = len(dartResult)

    square_dict = {'S': lambda x: x ** 1,
                   'D': lambda x: x ** 2,
                   'T': lambda x: x ** 3}

    while i < length:
        # 숫자 처리 (10 처리)
        if dartResult[i] == '1' and i + 1 < length and dartResult[i + 1] == '0':
            score = 10
            i += 1
        else:
            score = int(dartResult[i])

        i += 1

        # S, D, T 처리
        if dartResult[i] in square_dict:
            score = square_dict[dartResult[i]](score)
            stack.append(score)

        i += 1

        # * 또는 # 처리
        if i < length and dartResult[i] in ['*', '#']:
            if dartResult[i] == '*':
                stack[-1] *= 2
                if len(stack) > 1:
                    stack[-2] *= 2
            elif dartResult[i] == '#':
                stack[-1] *= -1
            i += 1

    return sum(stack)


# 테스트 케이스
print(solution("1S2D*3T"))  # 출력: 37
print(solution("1D2S#10S"))  # 출력: 9
print(solution("1D2S0T"))  # 출력: 3
print(solution("1S*2T*3S"))  # 출력: 23
print(solution("1D#2S*3S"))  # 출력: 5
