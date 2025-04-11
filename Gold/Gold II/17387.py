"""
선분위에 다른 선분위의 점의 내적값이 0이상이거나 해당 선분의 길이 ^ 2 이하여야 하는데
0보다 크다고 조건을 둬서 틀리고있었다.
32412	40
"""

def op(a, b):
    k = a[0] * b[1] - a[1] * b[0]
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def dp(a, b):
    return  0 <= a[0] * b[0] + a[1] * b[1] <= (a[0] ** 2 + a[1] ** 2)

def sol():
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x3, y3, x4, y4 = map(int, input().rstrip().split())

    v13 = x3 - x1, y3 - y1
    v12 = x2 - x1, y2 - y1
    v14 = x4 - x1, y4 - y1

    op1312 = op(v13, v12)
    op1214 = op(v12, v14)

    v32 = x2 - x3, y2 - y3
    v34 = x4 - x3, y4 - y3
    v31 = x1 - x3, y1 - y3

    op3234 = op(v32, v34)
    op3431 = op(v34, v31)
    
    if op1312 * op1214 > 0 and op3234 * op3431 > 0:
        print(1)
    elif (op1312 == 0 and dp(v12, v13)) or (op1214 == 0 and dp(v12, v14)):
        print(1)
    elif (op3234 == 0 and dp(v34, v32)) or (op3431 == 0 and dp(v34, v31)):
        print(1)
    else:
        print(0)

sol()

