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



