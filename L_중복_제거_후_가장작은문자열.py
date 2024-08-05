def remove_duplicate_letters(s):
    last_occurrence = {c: i for i, c in enumerate(s)}  # 각 문자의 마지막 위치 저장
    stack = []  # 결과를 저장할 스택
    seen = set()  # 스택에 있는 문자를 추적

    for i, c in enumerate(s):
        if c not in seen:  # 현재 문자가 스택에 없으면
            # 스택이 비어있지 않고, 현재 문자보다 사전적으로 더 큰 문자가 스택의 마지막에 있으며
            # 그 문자가 나중에 다시 등장할 수 있는 경우
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.discard(stack.pop())  # 스택에서 제거하고 집합에서도 제거
            stack.append(c)  # 현재 문자를 스택에 추가
            seen.add(c)  # 현재 문자를 집합에 추가
    return ''.join(stack)  # 스택을 문자열로 변환하여 반환
