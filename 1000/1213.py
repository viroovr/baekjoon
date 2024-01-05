from bisect import bisect_left, bisect_right
import string

u = string.ascii_uppercase
# print(u)AAABB
li = [0] * len(u)
name = sorted(list(input()))
# print(name)
even, odd = 0, 0
odd_alpha = None
for i, c in enumerate(u):
    k = bisect_right(name, c) - bisect_left(name, c)
    if k % 2 == 0:
        even += 1
    else:
        odd += 1
        odd_alpha = c
    li[i] = k

# print(li, even, odd)
ans = []
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    for i, x in enumerate(li):
        for _ in range(x // 2):
            ans.append(u[i])
    rev = ans[:]
    rev.reverse()
    if odd_alpha:
        ans.append(odd_alpha)
    ans.extend(rev)
    print("".join(ans))

# print(name)
