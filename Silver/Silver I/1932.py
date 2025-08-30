"""
실버까지의 문제는 이제 어떤 알고리즘으로 풀어야할지 떠오른다.

이중 배열을 활용해서 dp를 구현했지만
이전 열의 배열만 이용하고도 풀 수 있다.
36504	124 이중배열 dp
32412	116 단일 배열, 배열 치환
32412	112 단일 배열, 역순 순환
"""

from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(n):
    tri = list(map(int, input().split()))
    for j in range(i, -1, -1):
        right = dp[j] if i - 1 >= j else 0
        left = dp[j - 1] if i - 1 >= j - 1 >= 0 else 0
        dp[j] = tri[j] + max(left, right)

print(max(dp))