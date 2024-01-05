import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if len(string) == 1 and string[0] == '.':
        break
    st = []
    isyes = True
    for c in string:
        if c == '(' or c == '[':
            st.append(c)
        elif c == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                isyes = False
                break
        elif c == ']':
            if st and st[-1] == '[':
                st.pop()
            else:
                isyes = False
                break
    print("yes" if isyes and not st else 'no')
