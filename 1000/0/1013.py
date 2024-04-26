T = int(input())
# (100+1+ | 01)+
for _ in range(T):
    st = list(input())
    # print(st)
    fail = False
    count = 0
    while st:
        check = False
        temp = []
        temp.append(st.pop())
        if temp[-1] != '1':
            fail = True
            break
        while st:
            if st[-1] == '1':
                temp.append(st.pop())
                # print("pop 1", st)
            else:
                break
        else:
            fail = True
            break
        # print(st)
        if len(st) >= 2:
            temp.append(st.pop())
            # print(st)
            temp.append(st.pop())
            # print(st)
            # print(temp)
            if temp[-1] != '0' or temp[-2] != '0':
                check = True
            # print(st, check)
        else:
            check = True
        if not check:
            while st:
                if st[-1] == '0':
                    temp.append(st.pop())
                    # print("pop 0", st)
                else:
                    break
            else:
                fail = True
                break
            temp.append(st.pop())
            # print("te st", temp, st)
            if temp[-1] != '1':
                fail = True
                break
        else:
            st.extend(reversed(temp))
            # print(st)
            # print("temp:  ", temp)
            if st[-1] == '1' and st[-2] == '0':
                st.pop()
                st.pop()
                # print("01 pop", st)
            else:
                fail = True
                break

    if fail:
        # print(st)
        print("NO")
    else:
        # print(st)
        print("YES")
