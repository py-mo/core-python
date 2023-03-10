# list_name = [elements] -> separate elements by ,
# list_name = [element1, element2, ...]
# list can have a element


my_list = ['a']
print (my_list)
print (len(my_list))
print (type(my_list))

print ('-----------')

# Index in list is similar to string
my_list = ['a', 'b', 8, 'h', 1]
print (my_list[3])
print (my_list[1: 7])
print (my_list[1: 7: 2])
print (my_list[-2])
print (my_list[-1: -4: -2])

print('-----------')

# Concatenate two list
new_list = my_list + [10, 11, 12]
print (new_list)

new_list = [*my_list, *[10, 11, 12]]
print (new_list)

print('-----------')

# Copy
copied_list = my_list.copy()
newlist = my_list
print(copied_list)
print(newlist)

my_list[0] = 'AA'

print (my_list)
print (copied_list)
print (newlist)

print('-----------')

# List's method
my_list.append('end') # append(element) -> It adds element to the end
print (my_list)

my_list.pop(4) # It gives a index and deletes that index
print (my_list)

my_list.remove(8) # This method gives a value and finds it then deletes it.
print (my_list)

my_list.reverse()
print (my_list)

my_list.extend('11') 
# It gives a iterable then seperates iterable index by index and append(seperated value)
my_list.extend(['Python', 'Java', 'C#'])
print(my_list)

my_list.insert(0, 'First') # It gives 2 input, first index and second value
# Then adds value to given index
print (my_list)

my_list.sort()
print (my_list)
my_list.sort(reverse=True)
print (my_list)
# Important: To use sort all element must have similar type

print (my_list.index('h')) # This method gives a element and find its index
print (my_list.count('AA'))

my_list.clear() # It deletes all elements
print (my_list)