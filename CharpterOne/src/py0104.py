#coding=gbk
#��������֮��ľ���
#2018.10.29
import math
a1=float(input("�������һ�����x:"))
a2=float(input("�������һ�����y:"))
b1=float(input("������ڶ������x:"))
b2=float(input("������ڶ������y:"))
c1 = (a1-b1)*(a1-b1)
c2 = (a2-b2)*(a2-b2)
c = c1 + c2
c = math.pow(c, 0.5)#c = math.sqrt(c)
print("�����ǣ�",c)