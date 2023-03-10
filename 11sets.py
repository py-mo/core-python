# Set is sorted(first number second letter)
# Set cannot have some copy from one value
# Also it doesn't have index# set_name = {item1, item2, ...}
my_set = {'a', 2, 'c', 4, 4}
print (my_set)
print (type(my_set))
print (len(my_set))

print ('--------')

# Concatenate some sets
set1 = {1, 2, 10}
set2 = {10, 10, 11}
set3 = {1, 12}

con_set = {*set1, *set2, *set3}
print (con_set)

print('--------')

x = my_set.copy()  # like list and dict
my_set.remove('a')
print (x)

print('--------')

# Set's method
my_set.add('A') # add give item to th set
print (my_set)

my_set.pop() # It deletes first item
print (my_set)

my_set.update('hello') # Gives a iterable and seperates it index by index and add each item to set 
print (my_set)

my_set.remove('h') # Gives a item and deletes it
print (my_set)

my_set.clear() # Delete all item
print (my_set)
print (type(my_set))