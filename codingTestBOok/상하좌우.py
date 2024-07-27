N = int(input())
x, y = 1, 1
moving_plan = list(input().split())


def move(dx, dy):
    global x, y
    if 0 < x + dx < N + 1 and 0 < y + dy < N + 1:
        x = x + dx
        y = y + dy


for d in moving_plan:
    if d == 'R':
        move(1, 0)
    elif d == 'L':
        move(-1, 0)
    elif d == 'U':
        move(0, -1)
    elif d == 'D':
        move(0, 1)

print(y, x)
