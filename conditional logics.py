"""
CONDITIONAL LOGIC
"""

if 100>10:
    print("Hundred is greater than ten")
#important to keep track of space-
#there is intendent of 4 spaces then only python understand the next expression is under if

if 100<10:
    print("Hundred is greater than ten")
#will not give value as its a false expression



print ("it will always print") #here it is not related to if condition because lack of indentesion

if 100>10:
    print("Hundred is greater than ten")
value= 'green'
if value =='green':
    print('Go')

value= 'red'
if value =='red':
    print('stop')

#it only excute the code block under the if condition
#if i dont want to use"if condition " all the time

value= 'green'
if value =='green':
    print('Go')
else:
    print('wait')

#more than 2 conditions case then we will use elif
#elif basically the expression in elif can be executed if the previous condition is not true

value= 'orange'
if value =='green':
    print('Go')
elif value=='yellow':
    print('prepare to stop')
else:
    print('stop')

    

