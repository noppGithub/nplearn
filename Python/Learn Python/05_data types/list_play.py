scores = [44,48,55,89,34]
scores.append(100) # Append adds a new item to the end
print(scores) # [44, 48, 55, 89, 34, 100]
scores.insert(0, 34) # Inserts 34 to index 0
scores.insert(2, 44) # Inserts 44 to index 2
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100]
scores.extend([23]) # Extend takes an iterable (loopable items) and adds to end of list
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100, 23]
scores.extend([12,10])
print(scores) # [34, 44, 44, 48, 55, 89, 34, 100, 23, 12, 10]

languages = ['C', 'C#', 'C++']
languages.pop()
print(languages) # ['C', 'C#']
languages.remove('C')
print(languages) # ['C#']
languages.clear()
print(languages) # []

alphabets = ['a', 'b', 'c']
print(alphabets.index('a')) # 0 (Returns the index of the element in list
print(alphabets.count('b')) # 1 (counts the occurence of an element

numbers = [1,4,6,3,2,5]
numbers.sort() # Sorts the list items in place and returns nothing
print(numbers) # [1, 2, 3, 4, 5, 6]

#Python also has a built in sorting function that returns a new list
sorted_numbers = sorted(numbers) # note - this is not a method
print(sorted_numbers) # [1, 2, 3, 4, 5, 6]

numbers.reverse() # reverse the indices in place
print(numbers) # [6, 5, 4, 3, 2, 1]

numbers_clone = numbers.copy() # another approach is numbers[:]
print(numbers_clone) # [6, 5, 4, 3, 2, 1]

avengers = ['ironman', 'spiderman', 'antman', 'hulk']
cloned_avengers = avengers[::1] # very commonly used pattern
reversed_avengers = avengers[::-1] # discussing again because it is also very common
merge_avengers = ' '.join(avengers) # used to join list into string
print(cloned_avengers) # ['ironman', 'spiderman', 'antman', 'hulk']
print(reversed_avengers) # ['hulk', 'antman', 'spiderman', 'ironman']
print(merge_avengers) # ironman spiderman antman hulk

range_of_numbers = list(range(10)) # quickly generates a list of specific range
print(range_of_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
another_range = list(range(0,5)) # with start stop
print(another_range) # [0, 1, 2, 3, 4]

first,second,third = ['tesla','ford','ferarri']
print(first) # tesla
print(second) # second
print(third) # ferarri

a,*others = [1,2,3,4,5] # remaining values are stored in others
print(a) # 1
print(others) # [2, 3, 4, 5]

first,*others,last= [😄,😋,😠,😔,😉]
print(first) # 😄
print(others) # ['😋', '😠', '😔']
print(last) # 😉