def sol():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    def op(a, b):
        return a[0] * b[1] - a[1] * b[0] > 0
    
    v13 = x3 - x1, y3 - y1
    v12 = x2 - x1, y2 - y1
    v14 = x4 - x1, y4 - y1

    if (op(v13, v12) ^ op(v12, v14)):
        print(0); return
    
    v32 = x2 - x3, y2 - y3
    v34 = x4 - x3, y4 - y3
    v31 = x1 - x3, y1 - y3

    if (op(v32, v34) ^ op(v34, v31)):
        print(0); return
    
    print(1)
sol()


