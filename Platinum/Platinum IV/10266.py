"""
기준 선을 c1에서 잡은 뒤 c1의 최솟값을 기준으로 차이배열을 만들었다.
c1의 기준 선과 c2에서 같은 차이 가는 나는 요소를 찾아 동일한 기준으로 두게 하려고 시도했다.
하지만 차이를 N - 1개를 만들고 비교해서 시계방향, 반시계 방향까지 모두 커버가 안되어 실패했다.

일단, 차이에는 N - 1개가 들어가는게 아닌 N개가 들어가야 한다.
그리고 첫째 차이 리스트를 한번 이어 붙여, 두 번째 차이리스트와의 패턴 매칭을 시도한다.
KMP문제인줄 생각하는게 어려운것 같다.

61112	344
"""

def compute_lps(P):
    N = len(P)
    j = 0
    lps = [0] * N
    for i in range(1, N):
        while j > 0 and P[i] != P[j]:
            j = lps[j - 1]
        
        if P[i] == P[j]:
            j += 1
            lps[i] = j
    
    return lps

def get_possibility(N, c1, c2):
    M = 360_000
    c1.sort()
    c2.sort()

    diff1 = [(c1[i + 1] - c1[i] + M) % M for i in range(-1, N - 1)]
    diff2 = [(c2[i + 1] - c2[i] + M) % M for i in range(-1, N - 1)]

    T = diff1 + diff1
    P = diff2
    lps = compute_lps(P)

    lengthT = len(T)
    lengthP = len(P)
    j = 0
    for i in range(lengthT):
        while j > 0 and T[i] != P[j]:
            j = lps[j - 1]
        if T[i] == P[j]:
            j += 1
        if j == lengthP:
            return "possible"

    return "impossible"

def sol():
    N = int(input())
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    print(get_possibility(N, c1, c2))

sol()