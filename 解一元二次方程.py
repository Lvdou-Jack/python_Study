from math import *#为了使用开方函数
a = int(input("请输入二次项系数:"))
b = int(input("请输入一次项系数:"))
c = int(input("请输入常数项系数:"))
delta = b*b - 4*a*c
if delta < 0:
 print("该方程无解！")
else:
 delta = sqrt(delta)
 x1 = (-b+delta)/2*a
 x2 = (-b-delta)/2*a
 if delta == 0:
  print(x1)
 else:
  print("第一个解是:",x1,"第二个解是:",x2)