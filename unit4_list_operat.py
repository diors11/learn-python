#4.1集合的遍历
pizzaes = ['pepperoni pizza','chiken pizza','potato pizza']
for pizza in pizzaes:
	print(pizza)
	print(f"i like {pizza}!!\n")
print("i really like pizza!!\n")

#4.3数值列表的创建
#1:range()的使用
for value in range(1,21):
	print(value)

#2:列表推导式
values = [value for value in range(1,100001)]
#for value in values:
#	print(value)

#3:min() max() sum()
print(min(values))
print(max(values))
print(sum(values))


#4:range方法的步长
values = [value for value in range(1,20,2)]
for value in values:
	print(value)
values = [value for value in range(3,31,3)]
for value in values:
	print(value)
values = [value ** 3 for value in range(1,11)]
for value in values:
	print(value)
print(values)

#5:使用列表的切片
print('切片')
#列表的切片list[n:m]>返回第n到m-1个元素
lists = [value**2 for value in range(2,10,1)]
for list in lists[1:3]:
    print(list)
print('-------')
#复制列表list[:]返回整个列表元素
for list in lists[:]:
    print(list)
print('-------')
#返回列表后三个元素list[-3:]
for list in lists[-3:]:
    print(list)

#元组
#1
#自助餐 有一家自助式餐馆，只提供 5 种简单的食
#品。请想出 5 种简单的食品，并将其存储在一个元组中。
#使用一个 for 循环将该餐馆提供的 5 种食品都打印出来。
#尝试修改其中的一个元素，核实 Python 确实会拒绝你这样
#做。
dishes=('dish1','dish2','dish3','dish4','dish5')
for dish in dishes:
  print(dish)
print("\n")
#餐馆调整菜单，替换了两种食品。请编写一行给元组变量赋
#值的代码，并使用一个 for 循环将新元组的每个元素都打
#印出来。
dishes[0] = 'change1'
dishes[1] = 'change2'
for dish in dishes:
  print(dish)

