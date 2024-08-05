def solution(participant, completion):
    # 해시 테이블(딕셔너리) 초기화
    hash_table = {}

    # 참가자 목록을 해시 테이블에 저장
    for name in participant:
        if name in hash_table:
            hash_table[name] += 1
        else:
            hash_table[name] = 1

    # 완주자 목록을 통해 해시 테이블 갱신
    for name in completion:
        if name in hash_table:
            hash_table[name] -= 1

    # 해시 테이블에서 값이 1인 사람 찾기
    for name in hash_table:
        if hash_table[name] > 0:
            return name

