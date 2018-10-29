# coding=gbk
#勾股定理求斜边长度
#py0102.py
#2018.10.29
#
import math
a = float (input("请输入斜边1的长度："))#输入实数
b = float (input("请输入斜边2的长度："))
c = a*a + b*b
c = math.sqrt(c)
print("斜边长是：",c)