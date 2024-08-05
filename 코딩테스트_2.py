# 슬라이싱을 사용해서 코드 작성
"""def remove_adjacent_duplicates(s):
    index = 0
    while index < len(s):
        print(f"Index: {index}, Char: {s[index]}")
        if index > 0 and s[index - 1] == s[index]:
            print(f"Index {index - 1} 와 {index} 는 같은 문자열: {s[index]}")
            s = s[:index - 1] + s[index + 1:]
            print(f"중복 문자열 제거 후의 문자열: {s}")
            index = 0
        else:
            index += 1
    return not s
"""
# 스택을 사용해서 코드 작성
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 스택이 비어 있으면 True, 비어 있지 않으면 False 반환
    return not stack



    return s



result = remove_adjacent_duplicates("baabaa")
print(result)
result = remove_adjacent_duplicates("cdcd")
print(result)


# def remove_adjacent_duplicates(s):
#     stack = []
#     for char in s:
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
#     return not stack
#
# # 예시 사용
# result = remove_adjacent_duplicates("baabaa")
# print(result)  # True
# result = remove_adjacent_duplicates("cdcd")
# print(result)