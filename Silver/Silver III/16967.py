import sys
input = sys.stdin.readline

def get_A(H, W, X, Y, B):
    A = [[0] * W for _ in range(H)]

    for r in range(H):
        for c in range(W):
            A[r][c] = B[r][c]
            if X <= r and Y <= c:
                A[r][c] -= A[r - X][c - Y]
    
    for row in A:
        print(*row)
    
def sol():
    H, W, X, Y = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H + W)]
    
    get_A(H, W, X, Y, B)

sol()