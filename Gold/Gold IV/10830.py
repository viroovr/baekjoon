"""
1. 분할 정복을 이용한 빠른 거듭제곱 적용
    기존 코드에서는 B를 비트 단위로 나누어 미리 계산해 둔 행렬을 사용했지만,
    최적화 코드에서는 분할 정복 (O(log B))을 활용하여 필요한 연산만 수행
2. 공간 최적화
    dp 리스트를 제거하여 추가적인 메모리 사용을 최소화
    단위 행렬을 이용해 중간 결과를 효율적으로 저장
3. 코드 가독성 개선
    행렬 곱셈을 함수로 분리하여 가독성을 높이고 코드 중복 제거
조건에서 1000이하인 자연수 및 0이기 때문에 첫 행렬의 원소가 1000일때 0으로 반환됨을 고려해야 한다.
32412	40
32412	36  1,2,3
"""

def matrix_mult(A, B):
    return [[sum(A[r][k] * B[k][c] for k in range(N)) % 1000 for c in range(N)] for r in range(N)]

def matrix_pow(A, B):
    res = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while B:
        if B % 2:
            res = matrix_mult(res, A)
        A = matrix_mult(A, A)
        B >>= 1
    return res

def sol():
    global N
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    for row in matrix_pow(A, B):
        print(*row)

sol()