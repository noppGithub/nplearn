# combine text
print('Hello' + ' ' + 'World')

# number only
print(10+20)

# number and text
print('Hello ' + str(20))
print('Hello',20)

# separator
print('Hello','Separator')
print('Hello','Separator',sep='_')

# disable new line
from time import sleep
print('Downloading...10%', end='\r')
sleep(1)
print('Downloading...50%', end='\r', flush=True)
sleep(1)
print('Downloading...100%', end='\r', flush=True)
sleep(1)
print('Downloading...Completed!', end='\r', flush=True)