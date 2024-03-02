"""
Buit-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers

#previous range() function used to save them in the list,
but in Python 3 they have removed it. But in Python 2 as well,
there was another function called 'xrange()',
which used to do the same thing which range does in Python 3
"""

print(range(0, 10))

print(list(range(0, 10))) # by list command we are cast it into list to see the numbers

a= range(0,10)
print(a)
print(type(a))
print(list(a))

print('*'*20)

b= range(12,100) #different range
print(b)
print(type(b))
print(list(b))

print('*'*20)

#start , stop=None, step=none
b= range(10) #start #it generate the number for 0 to 9 #zero is default
print(b)
print(type(b))
print(list(b))

print('*'*20)
# step=none
b= range(10,20,2 ) #step #it will generate on the basis of step gap allocated
print(b)
print(type(b))
print(list(b))

print('*'*20)
# step=none
c= range(0,20,6) #step #it will generate on the basis of step gap allocated
print(c)
print(type(c))
print(list(c))

print('*'*20)

#for loop

l=[1,2,3]
for num in l:
    print(num)

print('*'*20)

l2=[1,2,3]
for num in range (3):
    print(num)

print('*'*20)

l3=[1,2,3]
for num in range (1,4):
    print(num)