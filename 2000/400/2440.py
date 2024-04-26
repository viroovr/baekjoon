import sys
p = sys.stdout.write
N = int(input())
for i in range(N):
    p('*' * (N - i))
    p('\n')
