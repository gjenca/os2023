#!/usr/bin/env python3

# str: ide cez znaky
for x in 'retazec':
    print(x)
print('------------')
# list: ide cez prvky
for x in ['ahoj',1,2,[1,2,3]]:
    print(x)
print('------------')
# tuple: ide cez prvky
for x in ('ahoj',1,2,[1,2,3]):
    print(x)
print('------------')
# set: ide cez prvky
for x in {'ahoj',1,2,(1,2,3)}:
    print(x)
print('------------')
# dict: ide po klucoch
d={'pes':4,'had':0}
for key in d:
    print(key,d[key])
print('------------')
# iterovanie cez dvojice
z=[(1,'a'),(2,'b'),(-3,'xxx')]
for t in z:
    print(t)
for n,s in z:
    print(n,s)
print('------------')
# enumerate
for i,item in enumerate(['ab','c','xxx']):
    print(i,item)
print('------------')
# dict.items
for key,val in d.items():
    print(key,val)





