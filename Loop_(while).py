"""
Execute statements repeatedly
conditions are used to stop the execution of loops
Iterable items are strings,list,tuple,dictionary
"""
#while loop- runs infinity
#use conditions to control the flow of loop

x=0
while x < 10:
    print('value of x is'+ str(x)) #this infinite loop
    print("one mor line") #we can write multiple line of codes #infinite loop
    x = x+1 #to stop contious run we can use a condition

l= []  #declare empty list
num = 0
while num < 10: #create while loop to add to the list
    l.append(num) #add to the list
    print('value of num is:' + str(num)) #to print everything again and again
    num+= 1  #increment num every time

    print(l)

