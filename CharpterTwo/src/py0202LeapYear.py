#coding=gbk
#判断闰年
#2018.10.31
year = input("请输入年份:")
y = int(year)
result = (y%4==0 and y%100!=0) or (y%400==0)
print("结果是:",result)