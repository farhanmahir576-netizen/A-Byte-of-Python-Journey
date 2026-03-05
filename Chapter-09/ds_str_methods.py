# This is a string object
name = 'Mahir'

if name.startswith('M'):
    print('Yes, the string starts with "M"')

if 'h' in name:
    print('Yes, it contains the string "h"')

if name.find('hir') != -1:
    print('Yes, it contains the string "hir"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
