# combine text
print('Hello' + ' ' + 'World')

# print number
print(10+20)

# print number and text
print('Hello ' + str(20))
print('Hello',20,sep='_')

# print to the same line
from time import sleep
print('Downloading....10%',end='\r')
sleep(1)
print('Downloading....29%',end='\r',flush=True)
sleep(1)
print('Downloading....40%',end='\r',flush=True)
sleep(1)
print('Downloading....56%',end='\r',flush=True)
sleep(1)
print('Downloading....100%',end='\r',flush=True)