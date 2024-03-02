"""
Iterating multiple lists at the same time
"""

l1 =[1,2,3]
l2 = [6,7,8,20,30,40]
#to work on 2 lists we defined 2 iterators a and b
for a,b in zip(l1,l2):
    print(a)
    print(b)

#zip is a built in function it will create a pair of element w
#when we pass two list inside it and it will stop at the end of the shorter list
#so what does that mean? if i have a list of length 3 and list of length 6
#The zip is going to start from the beginning but it is going to stop at the end of the shorter list.
#it gonna work only 3 times because it creates a pair and if doesn't find the pair for the next item in the shorter list it then just stops at that moment.

print('*'*20)
l3 =[0,1,2]
l4 = [6,7,8,10,20,30]
#to work on 2 lists we defined 2 iterators a and b
for a,b in zip(l3,l4):
  if a>b:
    print(a)
  else:
    print(b)