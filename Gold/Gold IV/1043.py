from collections import deque

def getMaxFalseStory(n, m, truth, parties):
    ret = 0
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for party in parties:
        for i in party:
            for j in party:
                graph[i][j] = 1
    q = deque(truth)
    mark = [False] * (n + 1)
    while q:
        p = q.popleft()
        for i in range(1, n + 1):
            if not mark[i] and graph[p][i] == 1:
                mark[i] = True
                q.append(i)
    for party in parties:
        for i in party:
            if mark[i]:
                ret -= 1
                break
        ret += 1
    return ret

def test_getMaxFalseStory(n, m, truth, parties, expected):
    a = getMaxFalseStory(n, m, truth, parties)
    assert expected == a, f"{expected} expected but {a}."

def sol():
    N, M = map(int, input().split())
    truth = list(map(int, input().split()))[1:]
    parties = [list(map(int, input().split()))[1:] for _ in range(M)]
    print(getMaxFalseStory(N, M, truth, parties))

def test_fun():
    test_getMaxFalseStory(5, 5, [4], [[1, 5], [2], [2, 3], [3, 4], [4, 5]], 0)
    test_getMaxFalseStory(4, 3, [], [[1,2],[3],[2,3,4]], 3)
    test_getMaxFalseStory(4, 1, [1], [[1,2,3,4]], 0)
    test_getMaxFalseStory(4, 1, [], [[1,2,3,4]], 1)
    test_getMaxFalseStory(4, 5, [1], [[1],[2],[3],[4],[4,1]], 2)
    test_getMaxFalseStory(10, 9, [1,2,3,4], [[1,5],[2,6],[7],[8],[7,8],[9],[10],[3,10],[4]], 4)
    test_getMaxFalseStory(8, 5, [1,2,7], [[3,4],[5],[5,6],[6,8],[8]], 5)
    test_getMaxFalseStory(1, 1, [1], [[1]], 0)
    test_getMaxFalseStory(1, 1, [], [[1]], 1)
    test_getMaxFalseStory(3, 4, [3], [[1],[2],[1,2],[1,2,3]], 0)
    test_getMaxFalseStory(3, 2, [1], [[1, 3], [2, 3]], 0)

if __name__ == "__main__":
    test = 0
    if test == 1:
        test_fun()
    else:
        sol()