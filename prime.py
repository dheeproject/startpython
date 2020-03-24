v=int(input("Enter a number"))
flag=0
for i in range(2,int(v/2)):
    if v%i==0:
        flag=1
        break
if flag==0:
    print("Input number is prime")
else:
    print("Input number is not prime")