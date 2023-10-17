s = input()
ls = len(s)
for i in range(ls):
    if s[i] != s[ls - i - 1]:
        print(0)
        break
else:
    print(1)
