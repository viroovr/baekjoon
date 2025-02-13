directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
direction_string = ["NORTH", "SOUTH", "EAST", "WEST"]
def adjust_coords_minus(c, s):
    u = s - 1
    q, r = divmod(c, u)
    return (abs(q) % 2 == 1), (u - r if abs(q) % 2 else r)

def adjust_coords_plus(c, s):
    u = s - 1
    q, r = divmod((c - 1), u)
    if q % 2 == 0:
        return False, r + 1 if u != 1 else 1
    else:
        return True, u - 1 - r

def log_shark(sharks):
    board = [[0] * C for _ in range(R)]
    for k, v in sharks.items():
        x, y = k
        board[y][x] = f"({v[0]},{v[1]}{direction_string[v[2]]})"
    for i in range(R):
        print(*board[i])
    print("=======")

def get_shark_sizes(sharks):
    sizes = 0
    for human_col in range(C):
        target = next(((x, y) for x, y in sorted(sharks.keys()) if x == human_col), None)
        if target:
            sizes += sharks.pop(target)[0]
        
        moved_sharks = {}
        for (x, y), (z, s, d) in sharks.items():
            dx, dy = directions[d]
            nx, ny = x + s * dx, y + s * dy
            is_reverse = False
            if nx < 0:
                is_reverse, nx = adjust_coords_minus(nx, C)
            elif C <= nx:
                is_reverse, nx = adjust_coords_plus(nx, C)
            if is_reverse:
                d = 3 - d + 2

            is_reverse = False
            if ny < 0:
                is_reverse, ny = adjust_coords_minus(ny, R)
            elif R <= ny:
                is_reverse, ny = adjust_coords_plus(ny, R)
            if is_reverse:
                d = 1 - d

            moved_sharks[(nx, ny)] = max(moved_sharks.get((nx, ny), (0, 0, 0)), (z, s, d), key=lambda t : t[0])
        sharks = moved_sharks
    return sizes

def sol():
    global R, C, M
    R, C, M = map(int, input().split())
    sharks = {}
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks[(c - 1, r - 1)] = (z, s, d - 1)

    print(get_shark_sizes(sharks))

sol()

# print(adjust_coords_plus(3, 3))
# print(adjust_coords_plus(4, 3))
# print(adjust_coords_plus(5, 3))
# print(adjust_coords_plus(6, 3))
# print(adjust_coords_plus(7, 3))
# print(adjust_coords_plus(8, 3))
# print(adjust_coords_plus(9, 3))
# print(adjust_coords_plus(10, 3))
# print(adjust_coords_plus(11, 3))
# print(adjust_coords_plus(12, 3))
# print(adjust_coords_plus(13, 3))
# print(adjust_coords_plus(14, 3))
# print(adjust_coords_plus(15, 3))
# print(adjust_coords_plus(16, 3))
# print("====")
# print(adjust_coords_plus(2, 2))
# print(adjust_coords_plus(3, 2))
# print(adjust_coords_plus(4, 2))
# print(adjust_coords_plus(5, 2))
# print(adjust_coords_plus(6, 2))
# print(adjust_coords_plus(7, 2))
# print(adjust_coords_plus(8, 2))
# print(adjust_coords_plus(9, 2))
# print(adjust_coords_plus(10, 2))