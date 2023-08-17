# P일 중 L일만 사용가능, 
# 5 8 20
# P = 8 L = 5 20
# v v v v v x x x v v v v v x x x v v v v
# P = 8 L = 5 17
# v v v v v x x x v v v v v x x x v
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    m = (V // P) * L
    n = V % P if V % P <= L else L
    count = m + n
    print(f"Case {i}: {count}")
    i += 1
