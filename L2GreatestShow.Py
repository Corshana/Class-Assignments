#Task 1
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 > number2 and number3:
    print (f"{number1} Is the largest number")
elif number2 > number1 and number3:
    print (f"{number2} is the largest number")
else:
    print(f"{number3} is the largest number")
#Task 2
if number1 < number2 and number1 < number3:
    print (f"{number1} Is the smallest number")
elif number2 < number1 and number3:
    print (f"{number2} Is the smallest number")
elif number3 < number1 and number2:
    print (f"{number3} Is the smallest number")

#Task 3
if number1 == number2 and number1 == number3:
    print ("All numbers are equal")
elif number1 == number2 or number1 == number3:
    print ("two numbers are equal")
elif number2 == number3:
    print ("two numbers are equal")
else:
    print ("numbers are equal")