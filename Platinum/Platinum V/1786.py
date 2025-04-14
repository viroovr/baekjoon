"""
prefix function이라고 불리는 패턴 매칭 함수 dp배열을 어떻게 설정해야할지
고민을 오래했다. 조건 분기마다 하기에는 너무 다양한 케이스들이 있어서 dp라는 특성의
이전 최적해를 사용하려 했으나, 결국 for문이 두번 되길래 안되는 줄 알았다.

하지만 j는 의 연산횟수는 총 M으로 O(M)이 된다.
아직은 잘 이해가 안된다.

83220	496
"""

def get_pattern(T, P):
    N, M = len(T), len(P)
    if N < M:
        print(0)
        return
    
    dp = [0] * M
    def comput_pi():
        j = 0
        for i in range(1, M):
            while j > 0 and P[i] != P[j]:
                j = dp[j - 1]

            if P[i] == P[j]:
                j += 1
                dp[i] = j
    comput_pi()

    # print(dp)
    i, sj = 0, 0
    res = []
    while i <= N - M:
        for j in range(sj, M):
            if T[i + j] != P[j]:
                break
        else:
            res.append(i + 1)
        if j > 0:
            sj = dp[j - 1]
            i += j - sj
        else:
            sj = 0
            i += j - sj + 1


    print(len(res))
    print(*res)

            
        
def sol():
    T = input()
    P = input()
    get_pattern(T, P)

sol()