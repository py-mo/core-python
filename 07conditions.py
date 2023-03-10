# if condition(Bool):
#   do something

x = 10
y = 11
condition = x < y

print (f"x < y: {condition}")
if x < y:
    print ("y is bigger than x.")

if condition:
    print ("y is bigger than x.")

print ("--------------")

# if + else
# if condition:
#   do something
# else:(if condition is False, It runs)
#   do something

if x > y:
    print ("x is bigger than y.")
else:
    print ("x isn't bigger than y.")

print("--------------")

# if + elif 
# if condition:
#   do something
# elif other_condition:(if condition is Flase, Program checks it)
#   do something
# elif other_consition2:(if condition and other condition are False)
#   do something
# ...
# esle:(if all conditions are False)
#   do something
# can use in end and some elif
if x > y:
    print ("x is bigger than y.")
elif x == y:
    print ("x is equal to y.")
elif x < y:
    print ("y is bigger than x.")
else:
    print ("Somethign is wrong.")

print("--------------")
# Important: For use else and elif we must have a if



# We can use if in if or else
a = -2
b = -3
if a > b:
    print ("a is bigger than b.")
    if a**2 > b**2:
        print ("a**2 is bigger than b**2.")
    elif a**2 == b**2:
        print ("a**2 is equal to b**2.")
    else:
        print ("b**2 is bigger than a**2.")
elif a == b:
    print ("a is equal to b.")
else:
    print ("a is smaller than b.")