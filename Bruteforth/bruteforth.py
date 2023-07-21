from itertools import permutations, combinations

v = [0, 1, 2, 3]

for i in permutations(v, 2):
    print(i)
print(" ")
for i in combinations(v, 2):
    print(i)
