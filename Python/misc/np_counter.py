from collections import Counter

# the input list
names = ["john", "jane", "dex", "john",]
cnt = Counter(names)
print(cnt)
print(cnt.most_common(2))
# how many johns?
print(f"There are {cnt['john']} johns in the list")

