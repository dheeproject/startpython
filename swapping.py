a=int(input("Enter first number"))
b=int(input("Enter second number"))
#printing numbers before swap
print("Numbers before swapping are:-", a, b)
#start swapping without using third number
a=a+b
b=a-b
a=a-b
#swapping completed
print("Numbers after swapping", a, b)
