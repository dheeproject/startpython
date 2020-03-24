x=int(input("Enter first number"))
y=int(input("Enter second number"))
count=0 #for counting number of common divisors
#now below checling for the commom divisors)
if x>y or x==y:
    z=y
else:
    z=x
print("Common factors are:-")
for i in range(1,z+1):
    if x%i==0 and y%i==0:
        print(i)
        count+=1
if count==1:
    print("Sorry! there is no common divisors other than 1 in between these numbers")
