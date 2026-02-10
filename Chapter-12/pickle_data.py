import pickle

shoplist = ['apple', 'mango', 'carrot']
f = open('shoplist.data', 'wb')
pickle.dump(shoplist, f)
f.close()

f = open('shoplist.data', 'rb')
storedlist = pickle.load(f)
print("Stored List:", storedlist)
f.close()
