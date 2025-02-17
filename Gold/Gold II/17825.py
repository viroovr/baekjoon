"""
1. 중복 탐색 방지 → (index, piece_poses) 조합이 동일하면 캐싱된 값 사용
2. 빠른 탐색 종료 → score가 더 낮은 경우, 이미 탐색한 경우라면 중단
3. 메모리 사용량 최적화 → 불필요한 연산을 줄여 실행 시간 감소
32544	420 
56476	328 1, 3
37084	64  1,2,3
"""
def get_max_score(index, piece_poses, score, tree):
    global max_score, cache

    key = (index, tuple(piece_poses))

    if key in cache and cache[key] >= score:
        return
    cache[key] = score

    if sum(pruning[:10 - index]) + score <= max_score:
        return

    if index == 10:
        if score > max_score:
            # print(cache)
            # print(f"tree : {tree}, score: {score}, pieces_poses = {piece_poses}")
            max_score = score
        return

    for i, v in enumerate(piece_poses):
        y, x = v
        if y == -1:
            continue
        
        ny, nx = y, x
        if y == 0 and (x + 1) in [5, 10, 15]: 
            ny = {5: 1, 10: 2, 15: 3}[x + 1]
            nx = 0
            
        nx = nx + dices[index]
        if nx >= degrees[ny]:
            if ny == 0:
                nx = nx - degrees[ny] + 3
                ny = 4
            elif 0 < ny < 4:
                nx = nx - degrees[ny]
                ny = 4

        if (ny, nx) in piece_poses:
            continue

        if nx < degrees[ny]:
            piece_poses[i] = (ny, nx)
            get_max_score(index + 1, piece_poses, score + board[ny][nx], tree + [i])
        else:
            piece_poses[i] = (-1, 21)
            get_max_score(index + 1, piece_poses, score, tree + [i])
        piece_poses[i] = (y, x)
                    

def sol():
    global board, dices, max_score, degrees, cache, pruning
    pruning = [40, 38, 36, 35, 34, 32, 30, 28, 27, 26]
    max_score = -1
    dices = list(map(int, input().split()))
    piece_poses = [(0, -1) for _ in range(4)]
    board = [
        list(range(2, 40, 2)), 
        [10, 13, 16, 19], 
        [20, 22, 24], 
        [30, 28, 27, 26],
        [25, 30, 35, 40]
    ]
    cache = {}
    degrees = list(map(len, board))
    get_max_score(0, piece_poses, 0, [])
    print(max_score)
sol()