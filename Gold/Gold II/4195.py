"""
맵을 사용해서 union하는 문제.
이전에 parent의 루트에는 음수값으로 사이즈 크기를 넣었는데 여기서는 key가
string이므로 그냥 크기를 넣어도 상관없음

그리고 union과정에서 두 트리 사이의 깊이를 비교해서 붙여야 find경로 압축이 가능함
하지만 이 문제는, 깊이가 아닌 전체 트리 노드 개수를 root에 저장하므로, 단순 비교가 더 빠름
68780	184
68780	188 두 tree사이에서 작은 깊이루트로 큰 깊이 루트 삽입
"""
import sys
def find(x):
    if isinstance(parent[x], str):
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    if a != b:
        parent[a] += parent[b]
        parent[b] = a
    return parent[a]

def sol():
    global parent
    data = sys.stdin.read().split("\n")
    idx = 0
    T = int(data[idx])
    result = []
    for _ in range(T):
        idx += 1
        F = int(data[idx])
        parent = {}
        for _ in range(F):
            idx += 1
            a, b = data[idx].split()
            parent.setdefault(a, 1)
            parent.setdefault(b, 1)
            root_a, root_b = find(a), find(b)
            result.append(str(union(root_a, root_b)))
    sys.stdout.write("\n".join(result)+"\n")

sol()