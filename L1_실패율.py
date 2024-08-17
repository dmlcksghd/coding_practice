# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

# 이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.


def solution(N, stages):
    fail_rates = []

    total_player = len(stages)

    for stage in range(1, N + 1):
        # 해당 스테이지에 도달한 플레이어 수
        players_at_stage = stages.count(stage)

        # 실패율 계산
        if total_player > 0:
            fail_rate = players_at_stage / total_player
        else:
            fail_rate = 0

        # 스테이지 번호와 실패율을 리스트에 추가
        fail_rates.append((stage, fail_rate))  # 리스트에 추가

        # 다음 스테이지를 계산하기 위해 total_player에서 현재 스테이지 플레이어 수를 빼줌
        total_player -= players_at_stage

    # 실패율을 기준으로 내림차순, 실패율이 같으면 작은 번호 스테이지 순서로 정렬
    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    # x는 fail_rates 리스트의 각 요소 (stage, fail_rate) 형태의 튜플
    # x[1] 은 튜플의 두번째 값인 fail_rate를 나타내고, x[0]은 첫번째 값인 stage를 나타냄
    # -x[1] : 실패율(fail_rate)의 내림차순으로 정렬하기 위해 음수로 변환
    # sort 함수는 기본적으로 오름차순으로 정렬하므로, 음수로 만들어 내림차순 효과를 냄
    # x[0] : 실패율이 같을 경우 스테이지 번호(stage)를 오름차순으로 정렬

    # 정렬된 스테이지 번호만 반환
    return [stage for stage, rate in fail_rates]


# 예시
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))  # [3, 4, 2, 1, 5]

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))  # [4, 1, 2, 3]
