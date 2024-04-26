import sys


def push(st, x):
    st.append(x)


def pop(st, _):
    if st:
        return st.pop()
    return -1


def size(st, _):
    return len(st)


def is_empty(st, _):
    return 1 if len(st) == 0 else 0


def top(st, _):
    return st[-1] if st else -1


def _command(com):
    if com == 1:
        return push
    elif com == 2:
        return pop
    elif com == 3:
        return size
    elif com == 4:
        return is_empty
    elif com == 5:
        return top


input = sys.stdin.readline
stack = []
N = int(input())
for _ in range(N):
    command = list(map(int, input().split()))
    command.append(0) if len(command) == 1 else None
    ans = _command(command[0])(stack, command[1])
    if ans is not None:
        print(ans)
