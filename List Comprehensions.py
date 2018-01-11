# -*-coding:utf-8-*-

#列表生成器
print('\n#列表生成器')

#生成 1*1 类似的列表
print('\n#生成 1*1 类似的列表')

# method1
print('\nmethod1  for')

L = []
for i in range(1,5):
    L.append(i*i)
print(L)

# method2
print('\nmethod2  ListComprehensions')
print([x*x for x in range(1,5)])



#双层循环生成列表
print('\n双层循环生成列表')
print([x+y for x in 'asd' for y in 'qwe' ])

# &此外还可以在循环之后添加判断
print('\n此外还可以在循环之后添加判断')
print([x + y for x in 'asd' if x != 'a' for y in 'qwe' if y != 'q'])
print(111)

