# list1 = ['apple', 'banana', 'pineapple']
# # list列表类型支持直接打印
# print(list1)
#
# my_list4 = ["张三",18,90.5,True]
# print(my_list4, type(my_list4))


# my_list1 = ["a","b","c","d","e","f"]
#
# print(my_list1[2:5]) # c,d,e

# names = ['孙悟空', '唐僧', '猪八戒']
# list1 = ['Tom', 'Rose', 'Jack']
# # 1、使用extend方法追加元素"Jennify"
# # names.extend("Jennify")
# names.extend(list1)
# print(names)

# names = ['薛宝钗', '林黛玉']
# # 在薛宝钗和林黛玉之间，插入一个新元素"贾宝玉"
# names.insert(1, '贾宝玉')
# print(names)

# names = ['Tom', 'Rose', 'Jack', 'Jennify']
# # 删除Rose
# del names[1]
# # 打印列表
# print(names)

# names = ['貂蝉', '吕布', '董卓']
# del_name = names.pop()
# # 或
# # del_name = names.pop(1)
# print(del_name)
# print(names)

my_list1 = ["a","b","c","d","c","e","f"]

# 查询
# index找到了返回第一次出现的索引；如果找不到，会抛出异常。index与字符串中的函数用法完全一样
# print(my_list1.index("c"))
# print(my_list1.index("c", 4, 5)) # 区间是[start,end)
#
# print("-"*50)
# print("a" in my_list1)
#
# print("-"*50)
# # 增加
my_list2 = ["小乔","鲁班","项羽"]
# # append：在原有列表的基础上，在末尾添加新元素
# print(my_list2.append("赵云"))
#
# print(my_list2)


# extend：在原有列表的基础上，在末尾添加新元素
# my_list2.extend("张飞") # 注意：这么写会将字符串分割
# my_list2.extend(["张飞"])
# my_list2.extend([1,2])


# print("-"*50)
# my_list2.insert(13,"李白")
# my_list2.insert(-1,"廉颇")
# print(my_list2)

print("-"*50)
# 除了使用extend将两个列表拼接起来以外，还可以直接使用+。+的核心区别是会得到一个新列表，原始的没有发生变化
my_list1 = [3,1,2]
my_list2 = [4,6,5]
my_list3 = [8,9,7]
result_list = my_list2+my_list1+my_list3
print(my_list1)
print(my_list2)
print(result_list)

print("-"*50)
my_list1 = ["a","b","c","d","c","e","f"]
# del my_list1[1]
# print(my_list1)


result = my_list1.pop(1)
print(result)
print(my_list1)


result = my_list1.pop(-1)
print(result)
print(my_list1)

my_list1.remove("a")
print(my_list1)

# my_list1.remove("x")
# print(my_list1)

my_list1[1] = 'xyz'
print(my_list1)


my_list1.reverse()
print(my_list1)

my_list1 = [3,1,2]
my_list1.sort()

result = my_list1[::-1]
print(result)

list1 = ['貂蝉', '大乔', '小乔']
for i in list1:
    print(i)


my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(my_list, type(my_list))
print(my_list[1],type(my_list[1]))
print(my_list[1][2])


students = [['张三', '李四'],['王五', '赵六'],['田七', '钱八']]
for i in students:
    print(i)