# print('hellw')



### 综合案例：使用for循环实现用户名+密码认证-作业

# 案例：用for循环实现用户登录

# ① 输入用户名和密码

# ② 判断用户名和密码是否正确（username='admin'，password='admin888'） 

# ③ 登录仅有三次机会，超过3次会报错 



# chance_count = 3

# for i in range(chance_count):
#   username = input('请输入用户名')
#   password = input('请输入密码')
#   if username == 'admin' and password=='admin888' :
#     print('登录成功')
#     break
#   else :
#     print('账号密码错误，请重新输入')


# print('登录次数用完了！')



for i in range(3):
  username = input('请输入用户名')
  password = input('请输入密码')
  if username == 'admin' and password=='admin888' :
    print('登录成功')
    break
  else :
    print('账号密码错误，请重新输入')
