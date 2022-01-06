# ====================================== numbers ======================================
my_num = 10
print(my_num,'is type:',type(my_num))

my_num2 = 2.2
print(my_num2,'is type:',type(my_num2))

my_calc1 = my_num * int('7')
print(my_calc1,'is type:',type(my_calc1))

my_calc2 = my_num + my_num2
print(my_calc2,'is type:',type(my_calc2))

# ====================================== string ======================================
my_text = 'hello nplearn'
print(my_text,'is type',my_text)

address = '333/27' + ' New York city, road number ' + str(30)
print(address)

version = 3.6
str_formatted = f"Use this in Python {version}+"
print(str_formatted)

message = "Use this method"
version = "3.5 and below"
str_formatted = "{x} if your are using {y}".format(x=message,y=version)
print(str_formatted)

message = "hello world"
a = message[0]
print(a)

a = message[:1]
print(a)

a = message[0:5]
print(a)

a = message[::-1]
print(a)

a = message[::2] #step 2
print(a)

a = message.upper()
print(a)

a = message.title()
print(a)

a = message.split()
print(a)

a = message.replace('o','X')
print(a)
