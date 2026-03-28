message="Hello python world!"
print(message)
message = "你好,python!"
print(message)

name = "Eric"
message = f"Hello {name},would you like to learn some Python today?"
print(message)

name = name.lower()
print(name)
name = name.upper()
print(name)
name = name.title()
print(name)

great_person = "Albert Einstein"
great_words = f'{great_person} once said,"A person who never made a mistake never tried anything new."'
print(great_words)

great_person = "\tAlbert Einstein\t\n"
print(great_person)
print(great_person.lstrip())
print(great_person.rstrip())
print(great_person.strip())

adress = "http://python_note.txt"
print(f"adress:{adress}")
adress = adress.removeprefix("http://")
print(f"adress:{adress}")
adress = adress.removesuffix(".txt")
print(f"adress:{adress}")

#整数加法
a = 1_000
b=2
print(f"1000 + 2**2 = {a+b**b}")
#浮点数-整数,结果为整数
c = 1_000.0
d = 10
print(f"1000.0 - 10 = {c-d}")
#包含浮点数的运算,结果为浮点数,除法结果也是浮点数
#整数乘法
print(f"100*100={100*100}")
#整数除法
print(f"100/100={100/100}")
#整数乘浮点数
print(f"0.1*0.2={0.1*0.2}")
#浮点数/浮点数,结果为浮点数
print(f"0.2/0.2={0.2/0.2}")

#python中常数的表示
MAX_AGE = 100
print(f"constant:{MAX_AGE}")
MAX_AGE = 1_000
print(f"constant:{MAX_AGE}")
