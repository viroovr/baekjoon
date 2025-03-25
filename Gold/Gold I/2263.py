"""
재귀적으로 왼쪽 tree, 오른쪽 tree를 나눠서 접근했다.
inorder의 index접근이 시간초과를 일으켜서 map을 생성해서 풀리도록 변경했다.
86860	448

in_order와 pos_order를 순회하면서 바로 preorder를 반환하도록 했더니 리스트를 처리하는게 오래걸리나보다
91196	16384

함수 recursion 스택을 사용하지 않고, 일반적인 stack을 사용해서 구현했다.
61056	176
"""
def get_preorder(n, in_order, post_order):
    in_order_map = {v: i for i, v in enumerate(in_order)}

    stack = [(0, n - 1, 0, n - 1)]
    result = []

    while stack:
        io_start, io_end, po_start, po_end = stack.pop()

        if io_start > io_end or po_start > po_end:
            continue

        root = post_order[po_end]
        result.append(root)

        root_index = in_order_map[root]

        ra = root_index - io_start

        stack.append((root_index + 1, io_end, po_start + ra, po_end - 1))
        stack.append((io_start, root_index - 1, po_start, po_start + ra - 1))
    
    print(*result)

def sol():
    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    get_preorder(n, in_order, post_order)

sol()