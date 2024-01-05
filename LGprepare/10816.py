import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
findcards = list(map(int, input().split()))
ans = [bisect_right(cards, card) - bisect_left(cards, card) for card in findcards]
print(*ans)