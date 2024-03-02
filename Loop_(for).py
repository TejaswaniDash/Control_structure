"""
Execute statements repeatedly
conditions are used to stop the execution of loops
Iterable items are strings,list,tuple,dictionary
"""
#strings for loop
my_string = "abcabc"

#for c in my_string:
    #print(c)
   # print(c, end=" ") #replace new line to combine everything in same line


#here in the syntax "for" is the keyword for "for loop "and "in" is the keywork to search anything inside the my_string
#c is the on the fly variable, so c is going to behave like an iterator
#c is goint to iterate over the string and access each and individual character inside the string.

for c in my_string:
   if c== "a":
       print ('A', end = " ")
   else:
        print(c, end=" ") #replace new line to combine everything in same line

print()

#list for loop
cars= ['bmw','benz','honda']
for car in cars:
    print(car)

nums= [1,2,3]
for n in nums:
    print(n*100)

print ("*"*20)

#dictionary for loop
d={'one':1, 'two':2, 'three':3}
for k in d:
    print(k + " "+str(d[k]))
#in the dictionary first accessing the key of the dictionary, then accessing the value of dictionary

print ("*"*20)
for k,v in d.items():
#herd.items gives us back both key and value
     print (k)
      print(v)

#tuplre is similar to list for loop