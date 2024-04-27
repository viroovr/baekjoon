def pellindrome(q):
    for i in range(len(q) // 2):
        if q[i] != q[len(q) - i - 1]:
            return 'no'
    else:
        return 'yes'


q = input()
while q != '0':
    print(pellindrome(str(int(q))))
    q = input()
