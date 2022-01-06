set_of_numbers = {1,2,3,4,5,5}
print(set_of_numbers) # {1,2,3,4,5}  (Only unique values are stored)

emails = ['samantha@hey.com', 'rock@hey.com', 'samantha@hey.com']
emails_set = set(emails)
unique_emails = list(emails_set)
print(unique_emails) # ['rock@hey.com', 'samantha@hey.com']

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
print(set_a.union(set_b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a | set_b) # same as above just a compact syntax

print(set_a.intersection(set_b)) # {4, 5}
print(set_a & set_b) # same as above

set_a.discard(1)
print(set_a) # {2,3,4,5}