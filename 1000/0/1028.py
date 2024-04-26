
def is_diamond(y, x, num, direct):
    print("depth, y, x", y, x)
    if mine[y][x] != '1':
        return num - 1
    if direct == -1:
        if 0 <= y + 1 < R and 0 <= x - 1 < C:
            left = is_diamond(y + 1, x - 1, num + 1, -1)
            y = y + 1
            x = x - 1
            direct = 1
            print("y, x, left, num", y, x, left, num)
        else:
            return num - 1
    if direct == 1 and mine[y][x] == '1':
        if 0 <= y + 1 < R and 0 <= x + 1 < C:
            right = is_diamond(y + 1, x + 1, num + 1, 1)
            right = num + 1
            num = right
            print("y, x, right", y, x, right)
        else:
            return num - 1
    global temp
    print("num: ", num)
    if num < temp:
        pass
    else:
        temp = max(temp, num)
        print("temp: ", temp)
    return num


# R행 C열
R, C = map(int, input().split())
mine = [input() for _ in range(R)]
ret = 0
for y in range(R):
    for x in range(C):
        temp = 0
        print("\ny, x", y, x)
        is_diamond(y, x, 1, -1)
        ret = max(ret, temp)
        print("temp", temp)
print("ret", ret)
