from math import gcd
a, b = map(int, input().split())
u = gcd(a, b)
print(u)
print((a // u) * b)