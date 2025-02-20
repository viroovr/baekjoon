"""
1. heapq 제거 & sort() 사용
    - heappush() & heappop()을 사용하던 방식에서, 리스트에 추가 후 sort()를 수행하도록 변경
    - 코드가 더 간결해지고, 작은 데이터셋(N ≤ 20)에서는 sort()가 더 빠를 가능성이 큼
2. 개선가능점
    - 좋아하는 사람 수가 동일한 인접 좌석에 경우, 이 조건에 상관없이 다음 조건인 빈좌석 조건을 따진다.
        이를 나누어서 처리하면 속도가 빨라질 것으로 예상.
	35508	116 
    32412	112 1
    32412	108 1, input
"""

def get_satisfaction_score(students, class_room):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    find_student = [0] * (N ** 2 + 1)
    for student in students:
        favorite_student = student[1:]

        dp = []

        for r in range(N):
            for c in range(N):
                if class_room[r][c] == 0:
                    empty_seat, fav_seat = 0, 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            if class_room[nr][nc] == 0:
                                empty_seat += 1
                            elif class_room[nr][nc] in favorite_student:
                                fav_seat += 1
                    dp.append((-fav_seat, -empty_seat, r, c))
        
        dp.sort()
        _, _, r, c = dp[0]
        class_room[r][c] = student[0]
        find_student[student[0]] = favorite_student

    total_sum = 0
    for r in range(N):
        for c in range(N):
            fav_seat = 0
            fav_student = find_student[class_room[r][c]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and class_room[nr][nc] in fav_student:
                    fav_seat += 1
            if fav_seat:
                total_sum += 10 ** (fav_seat - 1)

    return total_sum

def sol():
    global N
    N = int(input())
    students = [tuple(map(int, input().split())) for _ in range(N ** 2)]
    class_room = [[0] * N for _ in range(N)]
    print(get_satisfaction_score(students, class_room))
sol()