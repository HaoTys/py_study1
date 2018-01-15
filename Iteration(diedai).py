# -*-coding:utf-8-*-

q = 'sdfaadsf'
w = list(range(5))

# 循环输出全部
print('\n循环输出全部:')

# 非下标迭代
print('\n非下标迭代:')
for i in q:  # 按我的理解是  i可以理解为是q中的一个小元素
    print(i)
for i in w:
    print(i, len(w))

# 下标迭代
print('\n下标迭代')
for i in enumerate(q):
    print(i)
for i in enumerate(w):
    print(i)

# 感觉其作用配合 另一个参数效果更好，详情见下面的方法
print('\n感觉其作用配合 另一个参数效果更好，详情见下面的方法')
for i, i1 in enumerate(q):
    print(i, i1)
for i, i1 in enumerate(w):
    print(i, i1)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
print('\n请使用迭代查找一个list中最小和最大值，并返回一个tuple：')

mai = [0, 5, 2, 0, 123, 133, 1, 7, 6, 87]


def select(mai):
    max = 0
    min = 0
    m = mai[0]
    for i, i1 in enumerate(mai[:]):
        for j, j1 in enumerate(mai[:]):
            if (mai[i] < mai[j]):
                m = mai[i]
                mai[i] = mai[j]
                mai[j] = m
    return (mai[:1], mai[-1:])


print(select(mai))

print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111+\n\n\n\n")

a1 = list(range(1,10))
for i in a1:
    print(i)

for i,j in enumerate(a1):
    print(i,j)