# default dict as integer
from collections import Counter, defaultdict

# create the dict
d = defaultdict(int)

# let say we have some numbers
my_num = [1, 2, 3, 3, 4, 4, 4]

# loop through the numbers and add them to the dict
for num in my_num:
    d[num] += 1

print(d)

# try counter
c = Counter(my_num)
print(c)
print(c.most_common(4))
