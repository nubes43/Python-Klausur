import pickle
name=""
while name != "end":
    name = input("Name eingeben:")
    if name != "end":
        print(name)

with open('numbers.txt', 'w') as file:
    for i in range (1,11):
        file.write(f'{i}\n')
        
with open('numbers.txt', 'r') as file:
    txt = file.read()


with open('numbers.txt', 'r') as file:
    lst = file.readlines()

print(txt)
print(lst)

L = [1, 2, 3]
with open('liste.pcl', 'wb') as fobj:
    pickle.dump(L, fobj)
with open('liste.pcl', 'rb') as fobj:
    L2 = pickle.load(fobj)

print(L2)