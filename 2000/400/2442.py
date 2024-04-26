import sys

p = sys.stdout.write
N = int(input())
for i in range(N):
    for _ in range(N - i - 1):
        p(' ')
    for _ in range(2 * i + 1):
        p('*')
    p('\n')
