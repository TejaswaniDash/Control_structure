"""
Break: To break out of the closet enclosing loop
continue: Go to the start of the closest enclosing loop
"""

x= 0
while x < 10:
    print("value of x is:" + str(x))
    x= x + 1

    if x ==8:
        break
    print("this example is awesome")
    print("*"*20)
#when the value of x become 8 it doesnot print. it breakes out of the loop and go outside
#and then print the next command
print("just broke out of the loop")

x= 0
while x < 10:
    print("value of x is:" + str(x))
    x= x + 1

    if x ==8:
        continue
    print("this example is awesome")
    print("*"*20)
#value if 7 and doesnt print anything but continue to value is 8 the continue statetement
# goes back to front of the loop and it start from the beinnging of the loop

"""
While Else Statement
#exactly same to if-else
one difference the else block it executes anytime the loop condition is evaluated to false.
in case of if and else, else wouldn't execute if the if condition is correct.
in case of while loop else will always execute
"""
x= 0
while x < 10:
    print("value of x is:" + str(x))
    x= x + 1

   # if x ==8:
    #    break
    print("this example is awesome")
    print("*"*20)
else:
    print('just broke out of the loop')

#else will not execute is the loop is ends with a break



