import math


print("Hello! Welcome to Quad Equation Solver!")
print("A basic Quad Equation looks like a*x^2+b*x+c")
print("Please input the values for A, B and C!")

a_value = int(input("a: "))
b_value = int(input("b: "))
c_value = int(input("c: "))

a = a_value
b = b_value
c = c_value

answers = set() 

try:

    answers.add(
        ((-1*b)+math.sqrt((b*b)-4*a*c))/2*a
    )

    answers.add(
        ((-1*b)-math.sqrt((b*b)-4*a*c))/2*a
    )

except:
    print("The equation has no solution!")

if not answers == set():
    print(answers)
