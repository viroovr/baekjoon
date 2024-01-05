# from sys import stdin
# input = stdin.readline


# def solution():
#     N = int(input())
#     points = list(tuple(map(int, input().split())) for _ in range(N))
#     points.sort()
#     for i in range(N):
#         print(*points[i])


# solution()

import sys

def cond(dot):
    x, y = dot.split()
    return int(x) + int(y)/1000000

dots = sorted(sys.stdin.readlines()[1:], key=lambda x: cond(x))
print(dots)
print(''.join(dots))
