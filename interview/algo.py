# from collections import defaultdict
# from itertools import combinations
# n = 1000
# map = defaultdict(list)
# for c in range(1, n):
#     for d in range(1, n):
#         result = c ** 2 + d ** 2
#         map[result].append((c, d))

# for result, li in map.items():
#     for k in combinations(li, 2):
#         if k[0][0] == k[1][1]:
#             continue
#         print(k)

##################### 1.1 START #####################
# def check_redundancy(string):
#     n = 13
#     data = [list() for _ in range(n)]
#     # data = dict()
#     for ch in string:
#         key = ord(ch) % n
#         if ch in data[key]:
#             return True
#         data[key].append(ch)
#     return False


# def check_redundancy_no_data_structure(string):
#     li = [False] * 2 ** 10
#     for ch in string:
#         k = ord(ch)
#         if li[k]:
#             return True
#         li[k] = True


# print("True") if check_redundancy(input()) else print("False")
# print("True") if check_redundancy_no_data_structure(
#     input()) else print("False")
#####################   1.1 END #####################
##################### 1.2 START #####################
# def is_permutation(str1, str2):
#     n = 17
#     data = [list() for _ in range(n)]
#     for ch in str1:
#         key = ord(ch) % n
#         data[key].append(ch)
#     for ch in str2:
#         key = ord(ch) % n
#         try:
#             print(data)
#             data[key].remove(ch)
#         except ValueError:
#             return False

#     return True


# str1, str2 = input().split()
# print(True) if is_permutation(str1, str2) else print(False)
#####################   1.2 END #####################
#           1.3 START
# def change_space_code(str1):
#     if len(str1) == 0:
#         return -1
#     new_str = []
#     for i in range(len(str1)):
#         if str1[i] == ' ':
#             new_str.append('%20')
#         else:
#             new_str.append(str1[i])
#     return "".join(new_str)

# print(change_space_code(input()))

#           1.3 END
#           1.4 START
# def is_palindrome(str1: str):
#     str1 = str1.lower().replace(" ", "")
#     for i in range(len(str1) // 2):
#         j = len(str1) - i - 1
#         if str1[i] != str1[j]:
#             return False
#     return True


# print(is_palindrome(input()))
#           1.4 END
#           1.5 START
# str1, str2 = input().split()


# def is_edit_once(str1: str, str2: str):
#     # This is check function insert, delete, substitution occur below once

#     # Prechecking
#     if abs(len(str1) - len(str2)) > 1:
#         return False
#     # define longer or shorter ones
#     if len(str1) >= len(str2):
#         longer, shorter = list(str1), list(str2)
#     else:
#         longer, shorter = list(str2), list(str1)

#     count = 0

#     if len(str1) != len(str2):
#         for i in range(len(longer)):
#             if i >= len(shorter):
#                 shorter.append(longer[i])
#                 count += 1
#             if longer[i] == shorter[i]:
#                 continue
#             else:
#                 if count == 1:
#                     return False
#                 shorter.insert(i, longer[i])
#                 print(shorter)
#                 count += 1
#     else:
#         for i in range(len(longer)):
#             if longer[i] == shorter[i]:
#                 continue
#             else:
#                 if count >= 1:
#                     return False
#                 count += 1
#     return True


# print(is_edit_once(str1, str2))

#           1.5 END
#           1.6 START
# str1 = input()


# def compressing(str1):
#     new_str = []
#     temp = str1[0]
#     count = 0
#     for ch in str1:
#         if temp != ch:
#             new_str.append(temp)
#             new_str.append(str(count))
#             count = 1
#             temp = ch
#         else:
#             count += 1
#     new_str.append(temp)
#     new_str.append(str(count))
#     return "".join(new_str) if len(new_str) <= len(str1) else str1


# print(compressing(str1))

#           1.6 END
#           1.7 START
# def rotate_90(mat, N, direction):
#     for i in range(N):
#         for j in range(i + 1, N):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
#     if direction == 'r':
#         for m in mat:
#             m.reverse()
#     elif direction == 'l':
#         mat.reverse()
#     print(mat)


# N = 4
# mat = [[j + i*2 for j in range(1, N + 1)] for i in range(N)]
# print(mat)
# rotate_90(mat, N, 'r')
# 1 2 3
# 3 4 5
# 5 6 7

# 5 3 1
# 6 4 2
# 7 5 3

# 3 5 7
# 2 4 6
# 1 3 5

# 1 2 3 4
# 3 4 5 6
# 5 6 7 8
# 7 8 9 10

#           1.7 END
#           1.8 START
from collections import defaultdict


def zero_mat(mat, M, N):
    # MxN matrix
    zero_pos = defaultdict(set)
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                zero_pos[i].add(j)
    for y, x in zero_pos.items():
        for i in range(N):
            mat[y][i] = 0
        for k in x:
            for i in range(M):
                mat[i][k] = 0
    print(mat)


mat = [
    [1, 2, 3, 4, 0],
    [1, 2, 3, 0, 3],
    [1, 2, 3, 1, 3]
]
zero_mat(mat, len(mat), len(mat[0]))
#           1.8 END
#           1.8 START
#           1.8 END
