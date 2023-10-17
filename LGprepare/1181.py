N = int(input())
words = set(input() for _ in range(N))
words_dict = {i: [] for i in range(1, 51)}
for i in words:
    words_dict[len(i)].append(i)
for v in words_dict.values():
    for k in sorted(v):
        print(k)