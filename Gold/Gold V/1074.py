"""
✅ 최적화 내용 요약
for i in range(2), for j in range(2) 사용   if-else 문으로 분기 처리
div = 2 ** (N - 1)                          div = 1 << (N - 1) (비트 연산)
tot = R * C // 4	                        tot = div * div (불필요한 연산 제거)

✅ 시간복잡도 분석
원래 코드: O(4^N) (탐색 + 연산 중복)
최적화 코드: O(N) (한 번씩만 연산)

32544	36 최적화 전
32412	40 후
"""

def get_visit_num(N, r, c, offset, sr, sc):
    if N == 1:
        return offset + (r - sr) * 2 + (c - sc)
    
    div = 1 << (N - 1)
    tot = div * div
    if r < sr + div:
        if c < sc + div:
            return get_visit_num(N - 1, r, c, offset, sr, sc)
        else:
            return get_visit_num(N - 1, r, c, offset + tot, sr, sc + div)
    else:
        if c < sc + div:
            return get_visit_num(N - 1, r, c, offset + tot * 2, sr + div, sc)
        else:
            return get_visit_num(N - 1, r, c, offset + tot * 3, sr + div, sc + div)
                    

def sol():
    N, r, c = map(int, input().split())
    print(get_visit_num(N, r, c, 0, 0, 0))

sol()