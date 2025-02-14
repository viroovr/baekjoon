from collections import defaultdict
def r_operation(r, c, A):
    max_col_cnt = c
    operated_A = []

    for row in A:
        freq = defaultdict(int)
        for num in row:
            if num:
                freq[num] += 1
        
        new_row = []
        for k, v in sorted(freq.items(), key=lambda x: (x[1], x[0])):
            new_row.extend([k, v])
        
        max_col_cnt = max(max_col_cnt, len(new_row))
        operated_A.append(new_row)

    for row in operated_A:
        row.extend([0] * (max_col_cnt - len(row)))

    return operated_A, max_col_cnt

def transpose_matrix(A):
    return list(map(list, zip(*A)))

def logging(A, rows):
    for i in range(rows):
        print(*A[i])
    print("====")

def get_min_time_k(A):
    row_cnt, col_cnt = 3, 3
    for t in range(101):
        # logging(A, row_cnt)
        if 0 <= r < row_cnt and 0 <= c < col_cnt and A[r][c] == k:
            return t
        if row_cnt >= col_cnt:
            A, col_cnt = r_operation(row_cnt, col_cnt, A)
        else:
            A, row_cnt = r_operation(col_cnt, row_cnt, transpose_matrix(A))
            A = transpose_matrix(A)
    return -1

def sol():
    global r,c,k
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]
    r -= 1
    c -= 1
    print(get_min_time_k(A))

sol()