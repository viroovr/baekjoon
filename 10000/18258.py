import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write


def operation(com):
    global stack
    if com[0] == 'push':
        stack.append(com[1])
        return None
    elif com[0] == 'pop':
        if stack:
            return stack.popleft()
        return -1
    elif com[0] == 'size':
        return len(stack)
    elif com[0] == 'empty':
        if stack:
            return 0
        return 1
    elif com[0] == 'front':
        if stack:
            return stack[0]
        return -1
    elif com[0] == 'back':
        if stack:
            return stack[-1]
        return -1


N = int(input())
stack = deque()
for _ in range(N):
    command = input().strip().split()
    t = operation(command)
    if t is None:
        continue
    print(str(t) + '\n')
