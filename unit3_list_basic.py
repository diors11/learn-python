#将一些朋友的名字存储在一个列表中,并且将其命名为names.依次访问该列表的每个元素,从而将每个朋友的名字都打印出来
names = ["xiao ming","li hua","zhao wu"]
print(names[0].title())
print(names[1].title())
print(names[2].title())

#问候语 继续使用上一题中的列表,并不打印名字,而是为每个人打印一条消息.每条消息都包含相同的问候语,但是抬头为相应朋友的名字.
print(f'{names[0].title()},你好!')
print(f'{names[1].title()},你好!')
print(f'{names[2].title()},你好!')

#自己的列表 想想你喜欢的通勤方式,如骑摩托车或者开汽车,并创建一个包含多种通>勤方式的列表.根据该列表打印一系列有关这些通勤方式的陈述,如下所示:>
#	I would like to own a Honda motorcycle.
transport = ["bicycle","motorcycle","car"]
print(f'I would like to own a {transport[0]}.')
print(f'I would like to own a {transport[1]}.')
print(f'I would like to own a {transport[2]}.')

#练习 3.4：嘉宾名单 如果你可以邀请任何人一起共进晚餐（无
#论是在世的还是故去的），你会邀请哪些人？请创建一个列表，
#其中包含至少三个你想邀请的人，然后使用这个列表打印消息，
#邀请这些人都来与你共进晚餐.
print(f'{names[0].title()} {names[1].title()} {names[2].title()},诚邀共进晚餐!')

#练习 3.5：修改嘉宾名单 你刚得知有位嘉宾无法赴约，因此需
#要另外邀请一位嘉宾。
#以完成练习 3.4 时编写的程序为基础，在程序末尾添加函数
#调用 print()，指出哪位嘉宾无法赴约。
#修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉
#宾的姓名。
#再次打印一系列消息，向名单中的每位嘉宾发出邀请。
name = "li hua"
new = "tie dan"
names[1] = new
print(f"{name.title()}无法前来,将邀请{new.title()}来与大家共进晚餐!")
print(f'{names[0].title()} {names[1].title()} {names[2].title()},诚邀共进晚餐!')

#练习 3.6：添加嘉宾 你刚找到了一张更大的餐桌，可容纳更多
#的嘉宾就座。请想想你还想邀请哪三位嘉宾。
#以完成练习 3.4 或练习 3.5 时编写的程序为基础，在程序末尾
#添加函数调用 print()，指出你找到了一张更大的餐桌。
#使用 insert() 将一位新嘉宾添加到名单开头。
#使用 insert() 将另一位新嘉宾添加到名单中间。
#使用 append() 将最后一位新嘉宾添加到名单末尾。
#打印一系列消息，向名单中的每位嘉宾发出邀请。
names.insert(0,"gou shen")
names.insert(2,"hua hua")
names.append("hu zi")
print(f'{names[0].title()},{names[1].title()},{names[2].title()},{names[3].title()} {names[4].title()} {names[5].title()},诚邀共进晚餐!')
#练习 3.7：缩短名单 你刚得知新购买的餐桌无法及时送达，因
#此只能邀请两位嘉宾。
#以完成练习 3.6 时编写的程序为基础，在程序末尾添加一行
#代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
#使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾
#为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让
#该嘉宾知道你很抱歉，无法邀请他来共进晚餐。
#对于余下两位嘉宾中的每一位，都打印一条消息，指出他依
#然在受邀之列。
#使用 del 将最后两位嘉宾从名单中删除，让名单变成空
#的。打印该名单，核实名单在程序结束时确实是空的。
name = names.pop()
print(f'因为餐桌买小了,{name}将无法前来赴约!')
name = names.pop()
print(f'因为餐桌买小了,{name}将无法前来赴约!')
name = names.pop()
print(f'因为餐桌买小了,{name}将无法前来赴约!')
name = names.pop()
print(f'因为餐桌买小了,{name}将无法前来赴约!')
name = names[1]
del names[1]
print(f'欢迎{name}继续前来赴约!')
name = names[0]
del names[0]
print(f'欢迎{name}继续前来赴约!')
print(names)



#管理列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
#sort排序LIST.sort()默认顺序排序,reverse=true字母顺序相反排序且无返回值
cars.sort()
print(f"cars.sort():{cars}")
cars.sort(reverse=True)
print(f"cars.sort(revers=true):{cars}")

#sorted()返回一个排序后的列表,不会对列表本身顺序进行改变
cars = ['bmw','audi','byd','xiaomi']
print(f"sorted():{sorted(cars)}")
print(f"sorted(cars,reverse=true):{sorted(cars,reverse=True)}")
print(f"cars:{cars}")

#LIST.reverse()反向打印列表且五返回值
print(f"cars:{cars}")
cars.reverse()
print(f"reverse():{cars}")

#len()返回列表长度
print(f"len(cars):{len(cars)}")

#测试3.8
#放眼世界 想出至少 5 个你想去旅游的地方。
#将这些地方存储在一个列表中，并确保其中的元素不是按字
#母顺序排列的。
places = ['Beijing','Xian','Xinjiang','Nanji','Fenglan']

#按原始排列顺序打印该列表。不要考虑输出是否整洁，只管
#打印原始 Python 列表就好。
print(f"places:{places}\n")

#使用 sorted() 按字母顺序打印这个列表，不要修改它。
#再次打印该列表，核实排列顺序未变。
print(f"sorted(plcase):{sorted(places)}")
print(f"places:{places}\n")


#使用 sorted() 按与字母顺序相反的顺序打印这个列表，
#不要修改它。
#再次打印该列表，核实排列顺序未变。
print(f"sorted(places,reverse=True):{sorted(places,reverse=True)}")
print(f"places:{places}\n")

#使用 reverse() 修改列表元素的排列顺序。打印该列表，
#核实排列顺序确实变了。
places.reverse()
print(f"places.reverse():{places}")
print(f"places:{places}\n")


#使用 reverse() 再次修改列表元素的排列顺序。打印该列
#表，核实已恢复到原来的排列顺序。
places.reverse()
print(f"places.reverse():{places}")
print(f"places:{places}\n")

#使用 sort() 修改该列表，使其元素按字母顺序排列。打
#印该列表，核实排列顺序确实变了。
print(f"cars:{cars}\n")
cars.sort()
print(f"cars.sort():{cars}\n")

#使用 sort() 修改该列表，使其元素按与字母顺序相反的
#顺序排列。打印该列表，核实排列顺序确实变了。
print(f"cars:{cars}\n")
cars.sort(reverse=True)
print(f"cars.sort(reverse=True):{cars}\n")



#倒序取出索引list[-1],取出倒数第一个元素,列表为空时报错









