#coding=gbk
#回文数的判别
#2018.10.31
I1 = input("请输入一个四位数：")#输入的是字符串
I1 = int(I1)
a = I1//1000
b = I1//100%10
c = I1//10%10
d = I1%10
I2 = d*1000+c*100+b*10+a
result=(I1==I2)
print("回文数判断结果：",result)