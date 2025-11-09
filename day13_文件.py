# f = open('python.txt','w')
# f.write('学习python')
# f.close()

# f = open('python.txt','r')
# content = f.read()
# print(content)

f = open('read_test.txt','r')
# content = f.readline()
# print('c-',content)

# while True:
#   content = f.readline()
#   if len(content) > 0:
#     print('wc---',content)
#   else :
#     break

file_obj = open('read_test.txt','r')

# content = file_obj.read()
# content = file_obj.read(5)
# content = file_obj.read(3)
# print(content)

# content = file_obj.readline()
# print(content)
# print("-"*50)
# content = file_obj.readline()
# print(content)

# content = file_obj.readlines()
# print(content)
# print(type(content))


# 例如: 把 a.py文件 拷贝到 a[备份].txt 文件中

# 先读再写

# f = open('python.txt','r')

with open('python.txt','r') as f:
  content = f.read()
  print('c--',content)
  
  # f2 = open('day07/pyBackup.txt','w')
  # f2.writelines(content)
  # f2.close()

  with open('day07/Backup.txt','w') as f2:
    f2.writelines(content)


  
  