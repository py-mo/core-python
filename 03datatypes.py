"""
Type(var_name) returns the type of var_name
Types in Standard Python are "int", "float", "str", "list", "dict", "set", "tuple", "bool"
I use ": var_type" after var_name in definition, It's optional
"""

# Numbers: integer, float
# Integer
integer_num: int = 25
print (integer_num, type(integer_num))
# Float
float_num: float = 25.1
print (float_num, type(float_num))

# String: everything between ' ', " ", ''' ''', """ """
# ' ', " ", They are similar
word1: str = "Hello"
word2: str = 'world!'
print (word1, word2)
print (type(word1), type(word2))
# ''' ''', """ """, They are similar
text: str = """ Python is
a programming language """
print (text)
print (type(text))

# List => []
my_list: list = [1, 2, 3, "a", 'b', "abc"]
print (my_list, type(my_list))

# Dict => {key: value}
my_dict: dict = {"language": "Python", "born": 1991}
print (my_dict, type(my_dict))

# Set, unique values => {}
my_set: set = {1, 1, 2, 5, "a", 'abc'}
print (my_set, type(my_set))

# Tuple => ()
my_tuple: tuple = (1, 2, 3, 3, "a")
print (my_tuple, type(my_tuple))

# Bool => True or False
cond: bool = True
print (cond, type(cond))
