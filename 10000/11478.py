S = input()
ret = set()
for i in range(1, len(S) + 1):
    for j in range(len(S)):
        ret.add(S[j:j + i])
print(len(ret))
