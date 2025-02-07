"""
1. 불필요한 리스트 복사 제거
    cctvs.pop()을 제거하고 인덱스를 이용해 재귀적으로 호출하도록 변경 → 리스트 조작 비용 감소
2. CCTV 방향 사전 정의
    cctv_modes를 미리 정의하여 불필요한 모듈 연산(% 4) 제거 → 연산 속도 향상
3. 카운트 배열(monitor_count) 도입
    - 각 위치가 몇 개의 CCTV에 의해 감시되는지 추적
    - CCTV가 여러 개 겹쳐도 제대로 관리 가능
    - 감시된 구역을 0으로 바로 복구하는 문제 해결
4. 백트래킹에서 감시된 영역만 업데이트
    - 감시된 구역이 monitor_count == 1일 때만 zero_count를 감소
    - 백트래킹 시 monitor_count -= 1 후 0이 되면 원래 상태 복구
5. Deepcopy 제거로 성능 최적화
    - deepcopy를 사용하지 않고 O(1) 복구 가능
    - 시간 복잡도 감소
메모리(Kb)  시간(ms)
33712	    2616
33576	    200
"""
# 북, 동, 남, 서 
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cctv_modes = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def monitor_region(y, x, mode, monitor_count):
    global office
    monitored_position = []
    for d in mode:
        ny, nx = y + directions[d][0], x + directions[d][1]
        while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
            if office[ny][nx] == 0:
                if monitor_count[ny][nx] == 0:
                    office[ny][nx] = 7
                monitor_count[ny][nx] += 1
                monitored_position.append((ny, nx))
            ny += directions[d][0]
            nx += directions[d][1]
    return monitored_position

def get_min_blind_spots(idx, monitor_count, zero_count):
    global min_val, office
    
    if idx == len(cctvs):
        # print("-----")
        # print(f"min_val = {min_val}, zero_count = {zero_count}")
        # for i in range(n):
        #     print(*office[i])
        # print("-----")
        min_val = min(zero_count, min_val)
        return
    
    cctv_type, y, x = cctvs[idx]

    for mode in cctv_modes[cctv_type]:
        monitored_position = monitor_region(y, x, mode, monitor_count)
        get_min_blind_spots(idx + 1, monitor_count, zero_count - len(monitored_position))

        for my, mx in monitored_position:
            monitor_count[my][mx] -= 1
            if monitor_count[my][mx] == 0:
                office[my][mx] = 0

def sol():
    global n, m, min_val, cctvs, office
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]

    cctvs = [(office[i][j], i, j) for i in range(n) for j in range(m) if 1 <= office[i][j] <= 5]
    zero_count = sum(row.count(0) for row in office)
    
    monitor_count = [[0] * m for _ in range(n)]
    min_val = 8 * 8 + 1
    get_min_blind_spots(0, monitor_count, zero_count)
    print(min_val)

if __name__ == "__main__":
    sol()