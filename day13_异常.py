# todo: 猜数字异常
import random


target = random.randint(1, 100)

while True:

  try:
    userNum = int(input('请输入你猜的数字'))

    if target == userNum:
      print('命中！！')
      break
    elif target > userNum:
      print('太小了')

    else :
      print('太大了')

  except:
    print('请输入数字!')


