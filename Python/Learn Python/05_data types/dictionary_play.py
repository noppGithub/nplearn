user = {'name': 'Max', 'age': 40, 'married': False}
print(user['name']) # Max
print(user['married']) # False

abstract = {
 'first': 123,
 True: 'hello',
 777: [1,3,4,5]
}

print(abstract['first']) # 123
print(abstract[True]) # 'hello
print(abstract[777]) # [1,3,4,5]

sample = {
    'username': 'hisenberg',
    'username': 'james'
}
print(sample['username']) # james

house = {
    'rooms' : 4,
    'occupants': 2,
    'doors': 6
}
print(house['windows']) # KeyError: 'windows'
#instead
print(house.get('windows')) # None
print(house.get('windows', 5)) # 5 (This sets a default value if no value is found)

user = {'name': 'Raghav', 'age': 20, 'country': 'India'}
print('name' in user.keys()) # True
print('gender' in user.keys()) # False
print('Raghav' in user.values()) # True

cat = {
    'name': 'Tom',
    'greet': 'meow',
    'health': 100
}
cat_copy = cat.copy()
print(cat_copy) # {'name': 'Tom', 'greet': 'meow', 'health': 100}

cat.pop('name')
print(cat) # {'greet': 'meow', 'health': 100}

cat.clear()
print(cat) # {}

cat_copy.update({'name': 'Polo'})
print(cat_copy) # {'name': 'Polo', 'greet': 'meow', 'health': 100}
cat_copy.update({'color': 'Black'}) # adds key value if not present
print(cat_copy) # {'name': 'Polo', 'greet': 'meow', 'health': 100, 'color': 'Black'}