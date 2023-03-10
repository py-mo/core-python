# range -> (start -> default = 0, end, step -> default = 1)
range_num1 = range(10)
range_num2 = range(2, 20, 3)

print (range_num1)
print (list(range_num1))
print (range_num2)
print (list(range_num2))
print ('----------')



# for obj_name in iterable:
#   do something len(iterable) times
list_num = list(range(10))
print (list_num)

for obj in list_num:
    print (obj)

print('----------')



# for obj_name in range(x):
#   do something x times
for i in range(10):
    print (i)

print('----------')


# while bool_value:
#   do something until bool_value is True
bool_val = True

x = 0
while bool_val:
    print (x)
    x += 1
    if x >= 10:
        bool_val = False