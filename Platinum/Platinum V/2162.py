"""
첫 코드는 그저 CCW로 교차하는지 판단하고, union-find로 분리집합을 생성했다.
분리집합 생성을 O(N^2)으로 반복해서 했기에 비효율적이었던 것 같다.
하지만 N이 3000이므로 시간복잡도내에 가능하다고 일단 생각했다.

검색결과, sweeping algorithm을 사용해서 왼쪽부터 또는 위쪽부터 쓸어가듯이
선분을 탐색하는 알고리즘을 알게 됐다.

x값이 작은 것들을 먼저 조사하고 조사된 시작점들은 활성 상태에 넣는다.
그리고 순차하면서, 시작점이라면 조사중인것과 교차하는지 판단한다.
끝점이라면, 활성상태에서 제거한다.
그렇다면 선분이 모두 교차한다면 O(N^2) 이지만 평균적으로 더 빠르게 해결가능하다.

같은 x 좌표 일때 정렬 기준상 시작점을 먼저 처리되게 해야만
선분이 끝에서 겹칠 때도 처리가 가능하다.

딱히 효율을 신경을 안썼는데, 순차적으로 진행하는 지역 판단을 생각못했다.

33432	5772 O(N^2)
34456	604 sweep algorithm
"""
import sys
input = sys.stdin.readline

def ccw(v1, v2, v3):
    res = (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v3[0] - v1[0]) * (v2[1] - v1[1])
    if res < 0: return -1
    elif res > 0: return 1
    else: return 0

def is_in(ccw, p1, p2, p3):
    return ccw == 0 and min(p1, p2) <= p3 <= max(p1, p2)

def intersect(a, b, c, d):
    abc = ccw(a, b, c)
    abd = ccw(a, b, d)
    cda = ccw(c, d, a)
    cdb = ccw(c, d, b)

    if abc * abd < 0 and cda * cdb < 0:
        return True
    elif is_in(abc, a, b, c) or is_in(abd, a, b, d):
        return True
    elif is_in(cda, c, d, a) or is_in(cdb, c, d, b):
        return True
    return False

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        if parent[root_x] < parent[root_y]:
            parent[root_x] += parent[root_y]
            parent[root_y] = root_x
        else:
            parent[root_y] += parent[root_x]
            parent[root_x] = root_y

def get_group_cnt(N, segments, events):
    global parent
    
    parent = [-1] * N
    active = []

    for _, typ, idx in events:
        s1, e1 = segments[idx]
        if typ == 0:
            for j in active:
                s2, e2 = segments[j]
                if intersect(s1, e1, s2, e2):
                    union(idx, j)
            active.append(idx)
        else:
            active.remove(idx)
    
    print(sum(i < 0 for i in parent))
    print(-min(parent))

def sol():
    N = int(input())
    segments = []
    events = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().rstrip().split())
        segments.append(((x1, y1), (x2, y2)))
        events.append((min(x1, x2), 0, i))
        events.append((max(x1, x2), 1, i))
    
    events.sort()

    get_group_cnt(N, segments, events)

sol()