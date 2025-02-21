"""
1. 리스트 슬라이싱 제거 → directions[1:8:2] 대신 diagonals를 직접 선언
2. 클라우드 이동 연산 개선 → 리스트 컴프리헨션으로 이동 연산 단순화
3. 배열 값 변경 로직 개선 → marked 집합을 활용하여 기존 클라우드 제외 후 새로운 클라우드 생성
4. 불필요한 연산 제거 → original_amount 저장 없이 직접 마킹된 값만 피해서 클라우드 생성
5. input().split() 방향 1빼기 연산 파이프라이닝
	32412	156
    32412	156 1,5
    33432	168 1,2
    33432	208 1,2,3,4,5
"""

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonals = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

def get_water_amount(buckets, moving_method):
    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
    for d, s in moving_method:
        length = len(clouds)
        dr, dc = s * directions[d][0], s * directions[d][1]
        for k in range(length):
            nr, nc = (clouds[k][0] + dr) % N, (clouds[k][1] + dc) % N
            buckets[nr][nc] += 1
            clouds[k] = (nr, nc)
        
        for i in range(length):
            r, c = clouds[i]
            cnt = 0
            for dr, dc in diagonals:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and buckets[nr][nc] > 0:
                    cnt += 1
            buckets[r][c] += cnt

        original_amount = []
        for r, c in clouds:
            original_amount.append(buckets[r][c])
            buckets[r][c] = -1

        new_clouds = []
        for r in range(N):
            for c in range(N):
                if buckets[r][c] >= 2:
                    buckets[r][c] -= 2
                    new_clouds.append((r, c))

        for i in range(length):
            buckets[clouds[i][0]][clouds[i][1]] = original_amount[i]

        clouds = new_clouds

    return sum(map(sum, buckets))
 
def sol():
    global N, M
    N, M = map(int, input().split())
    buckets = [list(map(int, input().split())) for _ in range(N)]
    moving_method = [tuple((int(x) - 1, int(y))) for (x, y) in (input().split() for _ in range(M))]

    print(get_water_amount(buckets, moving_method))

sol()