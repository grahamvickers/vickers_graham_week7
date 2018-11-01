# Exploring functions and how to write them out
# Also finding out what they do


def greeting():
    # say hello
    print("hello from your fist function!")


# this is how you call or invoke a function
greeting()


def greetings(msg="Hello there!", num=0):
    print("Our function says", msg, "The second arg is", num)


greetings()
greetings("This is an argument", 1)
greetings("why are we arguing?", 2)


myVariableNumber = 0


def someMath(num1=2, num2=5):
    myVariableNumber = num1 + num2
    return num1 + num2


sum = someMath()
print("Our sum variable is:", sum, "myVariableNumber is also", sum)
