#coding=gbk
#��д��ĸת��ΪСд��ĸ
c = input("��д��ĸ:")
y = (c if (c>='a' and c<='z') else chr(ord(c)+32))
#���������if...else...  ��  x if y else z
print("��ĸ:",c,"ASII:",ord(c),"ת��Ϊ:",y,"ASII:",ord(y))