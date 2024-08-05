def solution(phone_book):
    phone = {}

    # 모든 전화번호를 해시 테이블에 저장
    for phone_num in phone_book:
        phone[phone_num] = True

    #  각 전화번호의 접두어가 존재하는지 확인
    for phone_num in phone_book:
        prefix = ""
        for digit in phone_num:
            prefix += digit
            # 자기 자신을 제외하고 접두어가 존재하는지 확인
            if prefix in phone and prefix != phone_num:
                return False

    return True