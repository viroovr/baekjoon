"""
1. new_fire_balls와 fireballs를 재사용하여 메모리 절약
2. map(sum, zip(*fireballs_list)) 대신 직접 for 루프 연산
3. 리스트 길이 (length)를 미리 변수에 저장하여 중복 연산 방지
4. sys.stdin.readline
	37500	368
    35532	332 1,2,3
    35712	264 1,2,3,4
"""

from collections import defaultdict
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
import sys
input = sys.stdin.readline

def decide_direction(fireballs_list):
    first_odd = fireballs_list[0][2] % 2

    for _, _, d in fireballs_list:
        if d % 2 != first_odd:
            return (1,3,5,7)
    return (0, 2, 4, 6)

def get_fireball_mass(fireballs):
    for _ in range(K):
        new_fire_balls = defaultdict(list)

        for (r, c), fireballs_list in fireballs.items():
            for m, s, d in fireballs_list:
                dr, dc = directions[d]
                nr, nc = (r + dr * s) % N, (c + dc * s) % N
                new_fire_balls[(nr, nc)].append((m, s, d))
        
        fireballs.clear()

        for (r, c), fireballs_list in new_fire_balls.items():
            length = len(fireballs_list)
            if length > 1:
                sum_mass, sum_speed = 0, 0
                for m, s, _ in fireballs_list:
                    sum_mass += m
                    sum_speed += s

                m = sum_mass // 5
                if m == 0:
                    continue

                s= sum_speed // length
                fireballs[(r, c)] = [(m, s, d) for d in decide_direction(fireballs_list)]
            else:
                fireballs[(r, c)] = fireballs_list
        
    return sum(m for fireballs_list in fireballs.values() for m, _, _ in fireballs_list)

def sol():
    global N, M, K
    N, M, K =map(int, input().split())
    fireballs = defaultdict(list)

    for _ in range(M):
        r,c,m,s,d = map(int, input().split())
        fireballs[(r - 1,c - 1)].append((m, s, d))
    
    print(get_fireball_mass(fireballs))

sol()