import random 

# random integer number
for _ in range(10):   
    x = random.randint(1, 10)
    print (x)

print ('----------')

# random number between 0 to 1
for _ in range(10):
    x = random.random() 
    print (x)

print ('----------')

# Choose a object in a list or a tuple or ...
my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')
for _ in range(5):
    print (random.choice(my_list), end = ' :')
    print (random.choice(my_tuple))

# ...