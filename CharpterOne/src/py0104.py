#coding=gbk
#计算两点之间的距离
#2018.10.29
import math
a1=float(input("请输入第一个点的x:"))
a2=float(input("请输入第一个点的y:"))
b1=float(input("请输入第二个点的x:"))
b2=float(input("请输入第二个点的y:"))
c1 = (a1-b1)*(a1-b1)
c2 = (a2-b2)*(a2-b2)
c = c1 + c2
c = math.pow(c, 0.5)#c = math.sqrt(c)
print("距离是：",c)