import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    orders = input().split()
    if orders[0] == 'push':
        if orders[1]:
            stack.append(orders[1])
    elif orders[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif orders[0] == 'size':
        print(len(stack))
    elif orders[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif orders[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
        