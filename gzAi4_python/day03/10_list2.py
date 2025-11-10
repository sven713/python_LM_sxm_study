# 给定列表original_list其中包含1, 2, 2, 3, 4, 4, 5, 6, 6, 7元素，现在通过编写程序对列表中的数据进行去重
result = []

source = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

for i in source:
    if i in result:
        print()
    else:
        result.append(i)

print(result)


my_tuple = (3,1,1,2)
print(my_tuple, type(my_tuple))

# my_tuple[1] = "hello"
# print(my_tuple)

print('--'*7)

# 给定一个元组my_tuple，里面包含1, 2, 3, 4, 5, 6, 7, 8, 9元素，要求统计数字元组中, 奇数的个数
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count = 0
for i in my_tuple :
    if i % 2 == 1 :
        count = count + 1
print(count)