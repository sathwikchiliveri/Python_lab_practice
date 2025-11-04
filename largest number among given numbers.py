num1=float(input("enter your first number: "))
num2=float(input("enter your second number: "))
num3=float(input("enter your third number: "))
num4=float(input("enter your fourth number: "))
if (num1 >= num2) and (num1 >=num3):
   largest=num1
elif (num2 >= num1) and (num2 >= num3):
    largest=num2
elif (num3 >= num1) and (num3 >= num2):
    largest=num3
else:
    largest=num4   
    print(num1,num2,num3,num4)
print("The largest number is",largest)
