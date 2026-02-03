#Error Handling and Debugging
# Error : an error is a problem that stops a program from working correctly. 
#Types of Error
#Syntax Error: Mistakes in the rule of programming language
# if X==0
#above miss : in the condition

# Runtime Errors 
#Error occurs while the program is  running
#Like Division by Zero
#File Open does not exist
#Accessing invalid indeex

#How to solve the Error Runtime Erro



#logical Error
#Program runs without error, but gives wrong output.
#like formula, addition, subtraction, multiplication



#Write a Python program to handle division by zero using `try` and `except`.

try:
        result=10/0
except ZeroDivisionError:
        print("Division by Zero is not Allowed")

#Multiple except

try: 
        number=int(input("Enter the number: "))
        result=10/number
except ZeroDivisionError:
        print("Zero Can't divide by the number")
except ValueError:
        print("Please the entered the number")

#Perform operation exception No occur
try:
        num=int(input("Enter the Number"))
        result=10/number
except ZeroDivisionError:
        print("Zero Can't by divide 10")
else:
        print("Result", result)

#finally block always runs, no matter what—whether an error occurs or not.

try: 
    num = 0 
    result = 10 / num 
except ZeroDivisionError: 
   print('Cannot divide by zero.') 
finally: 
    print('End of program.') 


#Custom error
def checkAge(age):
       if age<18:
              print("Not eligible for vote Age must be 18")
       else:   
              print("You are elgible for vote")
 
try:
       checkAge(15)
except ValueError as e:
       print(e)


try: 
    file = open('non_existent_file.txt') 
except FileNotFoundError: 
    print('File not found.')


file = open("data.txt", "r")
try:
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # always closes the file

try: 
    num = int(input('Enter a number: ')) 
    result = 10 / num 
except (ValueError, ZeroDivisionError): 
    print('Error: invalid input or division by zero.')


def check_positive(num): 
      assert num > 0, 'Number must be positive.' 
      print(f'{num} is positive.') 
check_positive(10) 
# check_positive(-5)  # This will raise an AssertionError 