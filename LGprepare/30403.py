from collections import defaultdict

rainbow = 'roygbiv'


def main():
    N = int(input())
    string = set(input())
    dic = defaultdict(int)
    for s in string:
        dic[s] += 1
    lower_rainbow = False
    for s in rainbow:
        if dic[s] == 0:
            break
    else:
        lower_rainbow = True
    upper_rainbow = False
    for s in rainbow.upper():
        if dic[s] == 0:
            break
    else:
        upper_rainbow = True
    if lower_rainbow and upper_rainbow:
        print("YeS")
    elif not lower_rainbow and not upper_rainbow:
        print('NO!')
    elif not upper_rainbow:
        print("yes")
    else:
        print("YES")


main()
