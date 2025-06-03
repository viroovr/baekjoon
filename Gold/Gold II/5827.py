"""
0-1 BFS로 flips가 전환되지 않은 것에 대해  우선 처리 해줘야 통과가 된다.
36516	264
"""
from collections import deque
import sys
input = sys.stdin.readline

def get_min_number(C, D, world):
    def fall(r, c, gravity):
        contact = False
        while True:
            nr = r + gravity
            if 0 <= nr < N and world[nr][c] != "#":
                if world[r][c] == "D":
                    contact = True
                r = nr
            else:
                break
        return contact, r, c

    visited = [[0] * M for _ in range(N)]
    contact, cr, cc = fall(C[0], C[1], 1)
    C = (cr, cc)
    if contact:
        return -1
    
    q = deque([(C[0], C[1], 1, 0)])
    visited[C[0]][C[1]] = 1

    while q:
        r, c, g, flips = q.popleft()
        if (r, c) == D:
            return flips
            
        if (r == N - 1 and g == 1) or (r == 0 and g == -1):
            continue

        gx = 1 if g == 1 else 2

        for dc in [-1, 1]:
            nc = c + dc
            if 0 <= nc < M and world[r][nc] != "#":
                contact, fr, fc = fall(r, nc, g)
                if contact:
                    return flips
                
                if not visited[fr][fc] & gx:
                    visited[fr][fc] |= gx
                    q.appendleft((fr, fc, g, flips))
                
        ng = -g
        ngx = 1 if ng == 1 else 2
        contact, fr, fc = fall(r, c, ng)
        if contact:
            return (flips + 1)
        if not visited[fr][fc] & ngx:
            visited[fr][fc] |= ngx
            q.append((fr, fc, ng, flips + 1))

    return -1

def sol():
    global N, M
    N, M = map(int, input().split())
    C, D = (-1, -1), (-1, -1)
    world = []
    for i in range(N):
        line = input().rstrip()
        world.append(list(line))
        for j in range(M):
            if line[j] == "C":
                C = (i, j)
            if line[j] == "D":
                D = (i, j)
    
    print(get_min_number(C, D, world))
    
sol()