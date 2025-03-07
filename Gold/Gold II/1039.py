"""
K가 최대 10, M이 최대 6인 조건에서, 브루트 포스 방법 K * M^4 ~= 10^4로 풀이가 가능함을 확인하고 빠르게 풀었다.
32412	48

그런데 알고리즘 카테고리가 너비 우선 탐색인걸 보고 해당 풀이에 대해 알아봤다.

💡 이 문제는 BFS (너비 우선 탐색) + 백트래킹을 사용하여 해결할 수 있다.
    - N을 문자열 형태로 변환 후, K번의 연산을 수행하면서 모든 가능한 숫자 조합을 탐색한다.
    - 각 단계에서 서로 다른 위치의 숫자를 swap하여 새로운 숫자를 만들고, 이를 큐에 삽입한다.
    - 중복 방지를 위해 visited 집합을 사용한다.
이 vistied 집합을 두어 계속 확인해야 하기 대문에 메모리와 시간 사용량이 더 길었다.
34952	72

질문 게시판에 그리디 알고리즘으로 푸는 사람이 있어서 조사해봤다.
그리디 접근이 어려운 이유
    1. 스왑 횟수(K)에 따라 최적의 선택이 달라짐
        - 그리디는 한 번의 선택이 이후에도 최적이 되어야 함
        - 하지만 이 문제에서는 K번의 교환을 고려해야 하므로, 최적의 선택이 바뀔 수 있음
"""
def get_max_number():
    n = tuple(str(N))
    M = len(n)
    k_numbers = {n}

    for _ in range(K):
        new_numbers = set()
        for k in k_numbers:
            k_list = list(k)
            for i in range(M):
                for j in range(i + 1, M):
                    if i == 0 and k_list[j] == '0':
                        continue
                    k_list[i], k_list[j] = k_list[j], k_list[i]
                    new_numbers.add(tuple(k_list))
                    k_list[i], k_list[j] = k_list[j], k_list[i]
        if not new_numbers:
            print(-1)
            return
        k_numbers = new_numbers
    
    print("".join(max(k_numbers)))
    
N, K = map(int, input().split())
get_max_number()