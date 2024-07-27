import sys
input = sys.stdin.readline
N = int(input())


def q_pop(q):
    if q:
        print(q.pop(0))
    else:
        print(-1)


def q_terminal(q, index):
    if q:
        print(q[index])
    else:
        print(-1)


q = []
for _ in range(N):
    command = input().split()
    if len(command) == 1:
        c = command[0]
        if c == 'pop':
            q_pop(q)
        elif c == 'size':
            print(len(q))
        elif c == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif c == 'front':
            q_terminal(q, 0)
        elif c == 'back':
            q_terminal(q, -1)
    else:
        q.append(command[1])
