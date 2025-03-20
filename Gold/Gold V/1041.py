"""
처음 문제보고 압도적인 N크기에 대한 N^3, 그리고 주사위에 대한 막연한 두려움이 문제가 어려울거라고 생각하게
만들었다.
하지만 막상 분석해보니, 간단한 문제였다.
역시 눈과 편도체에 의존하면 안된다.

32412	36
"""

from itertools import combinations

def get_min_side(N, numbers):
    if N == 1:
        return sum(numbers) - max(numbers)
    A, B, C, D, E, F = 0, 1, 2, 3, 4, 5
    INF = 50 * 6 + 1

    count1 = min(numbers)

    count2 = INF
    for x, y in combinations(range(6), 2):
        if (x, y) == (A,F) or (x, y) == (B,E) or (x, y) == (C,D):
            continue
        count2 = min(count2, numbers[x] + numbers[y])

    count3 = INF
    for x,y,z in [(A,B,C), (A,C,E), (A,E,D), (A,B,D), (F,E,C),(F,C,B),(F,B,D),(F,D,E)]:
        count3 = min(count3, numbers[x] + numbers[y] + numbers[z])

    return count1 * (N - 2) * (5 * N - 6) + count2 * (8 * N - 12) + count3 * 4

def sol():
    N = int(input())
    numbers = list(map(int, input().split()))
    print(get_min_side(N, numbers))

sol()