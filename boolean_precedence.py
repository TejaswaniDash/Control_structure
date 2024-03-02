"""
how can we evaluate when we have an expression with all the boolean operators i.e. and, or and not
Not evaluated from left to right. Order is
Not
and
or
"""

bool_output= True or not False and False
#not false-->True, True and False---> False, True or false--->True
print(bool_output)

bool_output1= 10==10 or not 10>10 and 10>10
print(bool_output1)
#using parenthesis we are giving an order to the expression to evaluate them in order
bool_output2= (10==10 or not 10>10) and 10>10
#not false-->True,  True or True--->True, True and False---> False,
print(bool_output2)