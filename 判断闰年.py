year = input("请输入年份:")#输入的是字符串
y = int(year)              #字符串转换为整数
result = (y%4==0 and y%100!=0) or (y%400==0)
print("结果是:",result)
