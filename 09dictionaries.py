# dict_name = {key1: value1, key2:value2, ...}
# dictionaries can be empty

my_dict = {}
print (my_dict)
print (type(my_dict))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print (my_dict)

print ('----------')

# Call elements
print (my_dict['b']) # dict_name[key_name] -> show value of given key
print (my_dict.get('b')) # show value of given key

print('----------')

# Concatenate dictionaries
dict2 = {'e': 5, 'f': 6, 'g': 7}

concatenated_dict2 = {*my_dict, *dict2}
print (concatenated_dict2)

print('----------')

# Copy
copied_dict = my_dict.copy()
new_dict = my_dict

my_dict['a'] = 100 # If we change dict, The dict that created by copy doesn't change but the dict that created without copy ,changes.

print (copied_dict)
print (new_dict)

print('----------')

# Dictioary's methods
print (my_dict.get('op')) # It gives a key_name and returns value of given key
# and if dict doesn't have a key_name returns None

my_dict.update({'A': 8}) # add given element to the end of dict
print (my_dict)

print (my_dict.values()) # It returns all values
print (my_dict.keys()) # It returns all keys
print (my_dict.items()) # It return all item(key and value together)

my_dict.pop('a') # It gives a key and deletes key's item
print (my_dict)

my_dict.popitem() # It deletes last item of dict
print (my_dict)

my_dict.clear() # It deletes all items
print (my_dict)