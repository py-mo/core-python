# String 
# var_name = "content" or '' or ''' ''' or """ """

# '' and "" for 1 line
text1 = "a1"
text2 = 'a2'

print (text1)
print (text2)
print (type(text1))
print (type(text2))
print ('----------')


# ''' ''' and """ """ for more than 1 line
p1 = '''Hello
This is Python'''

p2 = """Let's go
Python is one of the best programming languages."""

print (p1)
print (p2)
print (type(p1))
print (type(p2))
print('----------')

# Give lenght of your string
my_str = '123456789'
print(len(my_str))  # 9
print('----------')

# Indexes -> str_name[number of string]
# Indexes start form 0 -> hello -> h 0, e 1, l 2, l 3, o 4
print (p1[2])

# str_name[x: y] -> x to y-1
print (p2[1: 6])

# str_name[x: y: z] -> x -> start, y-1 -> end, x -> step
print (p2[1:20:2])

# str_name[minus_number] -> start from end
# hello -> 0 -1, l -2, l -3, e -4, o -5 
print (text1[-1])
print (p2[-10: -2: 2])

print('----------')


# str + str
new_str = my_str + text1
print (new_str)
print('----------')

# Join -> str.join(iterable) -> str + iterable[0] + str + iterable[1] + ...
my_list = ['a', 'b', 'c']
new_str2 = my_str.join(text2)
new_str3 = my_str.join(my_list)

print (new_str2)
print (new_str3)
print('----------')

# String's method
new_str3 = 'a1B2c3D4bB5'

print (new_str3.capitalize()) # It makes first letter uppercase and other lowercase
print (new_str3.upper()) # It makes all letters lowercase
print (new_str3.lower()) # It makes all letters uppercase

print (new_str3.find('B')) # Return index of given element that is goes sooner than other
print (new_str3.index('B')) # .index -> .find

print (new_str3.isdigit()) # Are all elements number?

print (new_str3.islower()) # Are all letter lowercase?
print (new_str3.isupper()) # Are all letter uppercase?

print (new_str3.split('B')) # It seperate to lists acoording to given element
