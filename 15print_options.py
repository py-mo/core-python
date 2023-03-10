text = 'Hello world!'


# Show variable in output -> print (var_name)
print (text)
print ('Hello Python.')

# Use custom string and variable in print
print (text, ' and Python.')

# If they are string
print (text + ' and Python.')


# {} -> print (f'text{var_name}text')
print (f"{text} and Python.")

# format print ("text{}text".format(var_name))
print ('{} and Python.'.format(text))
print ('----------------')

# go to next line and create a tab
print ("Go to next line\nNow we are in next line.")
print ("Create a tab space\tNow we create a tab.")
print('----------------')

# add something to end -> print ('...', end = "something")
print ("Finish.", end = '\nNot finished')