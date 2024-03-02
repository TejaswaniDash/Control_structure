"""
and
******************
True and True ---> True
True and False ---> False
False and False ---> False
********************

Or
*********************
True and True ---> True
True and False ---> True
False and False ---> False
***********************

not
************************
not True ---> False
not False ---> True
"""

and_output1 = (10==10) and (10>9)  #True and True ---> True
print(and_output1)

and_output2 = (10==10) and (10<9)  #True and False ---> False
print(and_output2)

and_output3 = (10>10) and (10<9) #False and False ---> False
print(and_output3)


or_output1 = (10==10) or (10>9)  #True and True ---> True
print(or_output1)

or_output2 = (10==10) or (10<9)  #True and False ---> True
print(or_output2)

or_output3 = (10>10) or (10<9) #False and False ---> False
print(or_output3)

not_true= not (10==10)  #Not True ---> False
print(not_true)

not_false= not (10>10)  #Not False ---> True
print(not_false)