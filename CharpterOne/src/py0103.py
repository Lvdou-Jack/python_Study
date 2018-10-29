# coding=gbk
#输入球的半径计算球的表面积和体积
#2010.10.29
import math
r = int (input("请输入半径："))
s = math.pi*4*r*r
v = 4*math.pi*math.pow(r, 3)/3
print("表面积:",s)
print("体积：",v)