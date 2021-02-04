name='diaopandeng'
print('获取第一个字符%s'%name[0])
print('第一个字母大写%s'%name.capitalize())
a='            hello        '
print('去除空格%s'%a.strip())
print('去除左边空格%s'%a.lstrip())
print('去除右边空格%s'%a.rstrip())
b=a
print('a的内存地址%d'%id(a))
print('b的内存地址%d'%id(b))
c='wo shi yi ge xiao bai'
print(c.find('s'))#查找字符产中存在的字符
print(c.find('g'))#查找字符产中存在的字符
print(c.lower())#转换字符串的大小写
print(c.upper())#转换字符串的大小写
d=' 1 2 3 4 5 6 7 8 9'#切片
print(d[::-1])
print(d[::-2])
print(d[1:9])
print(d[1:])
print(d[:10])



