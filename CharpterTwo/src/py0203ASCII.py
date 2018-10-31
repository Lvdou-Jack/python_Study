#coding=gbk
#大写字母转换为小写字母
c = input("大写字母:")
y = (c if (c>='a' and c<='z') else chr(ord(c)+32))
#条件运算符if...else...  ：  x if y else z
print("字母:",c,"ASII:",ord(c),"转换为:",y,"ASII:",ord(y))