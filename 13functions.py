# function
# def func_name(inputs):
#   do something
#   return output (if had a output)
# for use
# func_name(inputs)

def say_hello(name):
    print (f"Hello {name}")

def plus(num1, num2):
    x = num1 + num2
    return x


say_hello("World")

a = plus(10, -2)
print (a)


# lambda
# func_name = lambda inputs:outputs
minus = lambda x,y: x-y

b = minus(20, 5)
print (b)