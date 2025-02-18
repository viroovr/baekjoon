"""
적용된 최적화 기법
1. 딕셔너리 사용 (sharks → dict)
    (row, col)을 키로 해서 빠르게 충돌 감지
    sharks.count((-1, -1, -1)) 대신 remaining_sharks 변수를 활용하여 속도 향상
2. 냄새 정보 갱신 방식 개선
    냄새를 남길 때 sharks.items()로만 순회
    매번 이차원 배열을 전체 탐색하지 않도록 개선
3. 중복 제거 로직 개선
    더 작은 번호의 상어만 남기고, 나머지는 제거
    기존 방식보다 for 루프 반복 횟수 줄임
4. 불필요한 continue 제거
    if r == -1: continue를 제거하고 sharks 리스트에서 미리 제거
    중복 검사 연산을 딕셔너리 활용해 줄임
32544	340
32412	148 1,2,3,4
"""
def logging_board(board):
    for row in board:
        print(*row)
    print("====")

def get_one_shark_remain_time(sharks, smells, remaining_sharks):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for t in range(1, 1001):
        for shark_id, (r, c, _) in sharks.items():
            smells[r][c] = (shark_id, t)

        new_position = {}
        for shark_id, (r, c, d) in sharks.items():
            moved = False
            for j in shark_dir_priority[shark_id][d]:
                dr, dc = directions[j]
                nr, nc = r + dr, c + dc
                if 0<=nr<N and 0<=nc<N and (smells[nr][nc][0] == -1 or t - smells[nr][nc][1] >= K):
                    new_position[shark_id] = (nr, nc, j)
                    moved = True
                    break
            
            if not moved:
                for j in shark_dir_priority[shark_id][d]:
                    dr, dc = directions[j]
                    nr, nc = r + dr, c + dc
                    if (0<=nr<N and 0<=nc<N) and smells[nr][nc][0] == shark_id:
                        new_position[shark_id] = (nr, nc, j)
                        break
        
        new_sharks = {}
        for shark_id, (r, c, d) in new_position.items():
            if (r, c) in new_sharks:
                remaining_sharks -= 1
                if shark_id > new_sharks[(r, c)][0]:
                    continue
            new_sharks[(r, c)] = (shark_id, d)
        
        sharks = {shark_id : (r, c, d) for (r,c), (shark_id, d) in new_sharks.items()}
        
        if remaining_sharks == 1:
            return t
    return -1

def sol():
    global N,M,K, shark_dir_priority
    N, M, K = map(int, input().split())
    sea = [list(map(int, input().split())) for _ in range(N)]
    cur_direction = list(map(int, input().split()))
    shark_dir_priority = [[list(map(lambda x: int(x) - 1, input().split())) for _ in range(4)] for _ in range(M)]

    sharks = {}
    for r in range(N):
        for c in range(N):
            if sea[r][c]:
                sharks[sea[r][c] - 1] = (r, c, cur_direction[sea[r][c] - 1] - 1)
        
    smells = [[(-1, -1) for _ in range(N)] for _ in range(N)]
    remaining_sharks = M

    print(get_one_shark_remain_time(sharks, smells, remaining_sharks))

sol()
    