from collections import OrderedDict


def solution(cacheSize, cities):
    # 캐시 크기가 0일 때는 모든 요청이 캐시 미스
    if cacheSize == 0:
        return len(cities) * 5  # 캐시 미스는 모두 5초 소요

    # 캐시를 비어 있는 OrderedDict로 초기화
    cache = OrderedDict()
    total_time = 0  # 실행 시간 계산용

    # 모든 도시 이름을 소문자로 통일
    cities = [city.lower() for city in cities]

    # 캐시 동작 수행
    for city in cities:
        if city in cache:
            # 캐시 히트 -> 캐시에서 해당 도시 갱신 (최근에 사용됨)
            cache.move_to_end(city)
            total_time += 1  # 캐시 히트 시 1
        else:
            # 캐시 미스 -> 캐시에 추가
            if len(cache) >= cacheSize:
                # 캐시가 가득 찬 경우 가장 오래된 항목 제거
                cache.popitem(last=False)
            cache[city] = True  # 새로운 항목 추가
            total_time += 5  # 캐시 미스 시 5

    return total_time


# 다른 풀이

# 예시
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 예상 출력: 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 예상 출력: 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 예상 출력: 60
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 예상 출력: 25


# 시간 복잡도
O(n)