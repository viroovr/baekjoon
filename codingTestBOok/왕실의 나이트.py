x, y = input()
y = int(y)
x = int(ord(x)) - int(ord('a')) + 1

Dx = [2, 2, -1, 1, -2, -2, -1, 1]
Dy = [-1, 1, 2, 2, -1, 1, -2, -2]

count = 0
for dx, dy in zip(Dx, Dy):
    if 0 < x + dx < 9 and 0 < y + dy < 9:
        count += 1

print(count)
