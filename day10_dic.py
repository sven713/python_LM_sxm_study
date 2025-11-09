my_dict_3 = {'ab':1,"b":2,"a":[9,8,7]} # 如果key的类型是字符串，需要使用引号包起来
print(my_dict_3)

my_dict = {1:"hello",2:"world",3.999:"python"}
print(my_dict, type(my_dict))


print('---'*20)

person = {'name':'王大锤', 'age':28, 'gender':'male', 'address':'北京市海淀区'}
# 2、使用clear()方法清空字典
person.clear()
# 3、打印字典
print(person)


print('---'*20)


person = {'name':'貂蝉', 'age':18, 'mobile':'13765022249'}
# 2、调用items方法获取数据，dict_items([('name', '貂蝉'), ('age', 18), ('mobile', '13765022249')])
print(person.items())

for key, value in person.items():
    print(f'{key}：{value}')

print('---'*20)


# 需求: 编写一个程序将字符串转换为字典例如:输入: '5=Five 6=Six 7=Seven'   输出: {'5': 'Five', '6': 'Six', '7': 'Seven'}

# 1. 字符串按空格切割
# 2. 数组元素按=分割

str = '5=Five 6=Six 7=Seven'
arr = str.split( )
print(arr)

dic = {}
for i in arr:
  kv = i.split('=')
  dic[kv[0]] = kv[1]

print(dic)