# e = list(filter(lambda x: x > 100, [-5, 200, 300, -10, 10, 1000]))
# print(e)
# e = list(map(lambda x: x ** 2, [-5, 200, 300, -10, 10, 1000]))
# print(e)
# from functools import reduce
# def doSum(x1, x2):
#     return x1 + x2
# x = reduce(doSum, [100, 122, 33, 4, 5, 6])
# print(x)

# x = range(6)
# print(list(x))
import pandas as pd

df = pd.DataFrame( [
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True],
])
df.columns = ['id', 'name', 'age', 'decision']
# print(df)
# select column
# print(df[['name', 'age']])
# print(df.iloc[:, 3])

# select row
# print(df.iloc[1:3, :])
# print(df[df.age > 30])
# print(df[(df.age<35) & (df.decision==True)])
import numpy as np

myMatrix = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(myMatrix)
print(type(myMatrix))
print(myMatrix.transpose())