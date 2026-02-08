bri = set(['brazil', 'russia', 'india'])

print('india' in bri) # True
print('usa' in bri)   # False

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri)) # True

bri.remove('russia')
print(bri & bric) # OR bri.intersection(bric)
