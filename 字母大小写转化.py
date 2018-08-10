#将大写字母转化为小写字母
c = input("请输入一个字符:")
y = (c if (c>='a' and c<='z') else chr(ord(c)+32))
print("字符:",c,"ASII:",ord(c),"转换为:",y,"ASII:",ord(y))