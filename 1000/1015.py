N = int(input())
P = [-1] * N
A = [(int(v), i) for i, v in enumerate(input().split())]
for i, x in enumerate(sorted(A)):
    P[x[1]] = i
string = " ".join(list(map(str, P)))
print(string)

