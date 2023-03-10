import datetime

now = datetime.datetime.now()
print (now)


print (now.day)
print (now.month)
print (now.second)

print ('---------')

start = datetime.datetime.now()

x = 0
for i in range(10_000):
    x += 1
print (x)

end = datetime.datetime.now()

print (end - start)

# ...