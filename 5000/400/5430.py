import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write


def operation(num_list: deque, p):
    R = 0
    for char in p:
        if char == 'R':
            R += 1
        else:
            if len(num_list) == 0 or num_list[0] == '':
                return 'error'
            if R % 2 == 0:
                num_list.popleft()
            else:
                num_list.pop()
    if R % 2 == 1:
        num_list.reverse()
    ret_string = '[' + ",".join(num_list) + ']'
    return ret_string


T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    num_list = deque((input().strip('[]\n').split(sep=',')))
    print(operation(num_list, p) + '\n')
