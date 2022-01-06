my_tuple = (1,2,3) # Can be any no of items
print(my_tuple[1]) # 2 (Values can be accessed just like lists)
print(1 in my_tuple) # True (Checks if element is present)

colors = ('red', 'orange', 'blue', 'yellow')
new_colors = colors[1:4]
print(new_colors) # ('orange', 'blue', 'yellow')

color_1,*others = colors # unpacking!
print(color_1) # 'red'
print(others) # ['orange', 'blue', 'yellow']

print(len(colors)) # 4
print(colors.count('red')) # 1 
print(colors.index('orange')) # 1