# tuple_name = (value1, value2, ...)
# Tuple can be empty

my_tuple = (1, 2, 3, 4, 5, 6, 7, 7)
print (my_tuple)
print (len(my_tuple))

# Tuple index is similar to Strings and Lists
print (my_tuple[1])
print (my_tuple[:5:2])

print ('---------')

# Concatenate Tuples
tuple2 = (6, 6, 6)

concatenated_tuple = my_tuple + tuple2
print (concatenated_tuple)

concatenated_tuple2 = (*my_tuple, *tuple2)
print (concatenated_tuple2)

concatenated_tuple3 = my_tuple.__add__(tuple2)
print (concatenated_tuple3)

print('---------')

# Tuple's methods
print (my_tuple.count(7))
print (my_tuple.index(5)) # It gives index and returns its value

print(my_tuple.__add__((10, )))

print('---------')

# Tuple with 1 item
# tuple_name = (item, )
one_item_tuple = ('A', )
print (one_item_tuple)
print (type(one_item_tuple)) # It's a tuple

not_tuple = ('A')
print (not_tuple)
print (type(not_tuple)) # It's a string