# program01.py

print('\nRequirement 1\n')
print('This is Program01 - Yolanda Gunter\n')

print('Requirement 2\n')
print('Please enter the information requested.\n')
name = input('Last name: ')
hometown = input('Hometown: ')
occupation = input('Occupation: ')
hobby = input('Hobby: ')

print('\nRequirement 3\n')
print('Hello {}!'.format(name))
print('From {}.'.format(hometown))
print('I hope you like being a(n) {}.'.format(occupation))
print('{} sounds like an interesting hobby.'.format(hobby))

print('\nRequirement 4\n')
print('Alternative Output\n')
print('Hello',name,'!')
print('From ' + hometown + '.')
print('I hope you like being a(n)', occupation)
print(hobby + ' sounds like an interesting hobby.')

print('\nRequirement 5\n')
print('More Options\n')
print('Hello1 ',name,'!') # note the spaces after commas in the output
print('Hello2 ',name,'!', sep='') # suppress separator (no spaces in output)
print('Hello3 ',name,'! ', end='', sep='') # suppress endline and separator
print('Hello4 ',name,'! ', end='', sep='') # suppress endline and separator
print('Hello5 ',name,'! ', end='', sep='') # suppress endline and separator

print('\n\nRequirement 6\n')
print('''Program 1 provided good syntax with comma understanding.
I had to read notes on Requirements 4 and 5 several times, lol.
Coding the examples is helping me learn by repitition.''')
