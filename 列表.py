lista=[1,2,3,'nihao','haha']#定义一个列表
#print(lista[0])#打印列表第一个元素
#print(lista[1:3])#从第二个打印到第三个前闭后开
#print(lista[1:])#从第二个打印到最后一个
#print(lista[::-1])#负数从右向左打印
#print(lista*2)#复制列表中元素
#print('追加前',lista)
#lista.append(666)
#print('追加后',lista)
#lista.append(['jiujiu'])#追加操作
#print(lista)
#lista.insert(33,'这是我插入的数据')#插入操作
#print(lista)
#lista.extend([44,55,66])#扩展操作
#print(lista)
#print('修改前',lista)
#lista[0]='peter'
#print('修改后',lista)
#print('修改前',lista)
#del lista[0]#删除列表第一个元素
#print('修改后',lista)
#print('修改前',lista)
#del lista[1:3]#删除从第二个元素到第三个元素
#print('修改后',lista)
#print('修改前',lista)
#lista.remove(3)#移除元素  参数是具体的数据值
#print('修改后',lista)
#lista.pop(0)#删除元素  参数是具体的数据项索引值
print(lista.index(1))#查找元素位置