num = int(input())
divisors = list(map(int, input().split()))
divisors.sort()
if num % 2 == 0:
    t = num // 2 - 1
    ans = divisors[t] * divisors[t + 1] 
else:
    t = num // 2
    ans = divisors[t] ** 2
print(ans)