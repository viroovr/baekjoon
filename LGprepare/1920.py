from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
for i in B:
    if bisect_right(A, i) - bisect_left(A, i) == 0:
        print(0)
    else:
        print(1)