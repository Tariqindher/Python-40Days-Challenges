print('Day 2: Basic Task Input and Output ')

age =22
print('Rignt now My age is', age)
update_age = age + 3
print('After Master My age will be', update_age)
print('-----------------------------------')
print('Calculator Task')
num1 = int(input('Enter 1st number:'))
num2 = int(input('Enter 2ndnumber:'))
sum = num1 + num2
product = num1 * num2
difference = num1 - num2
quotient = num1 / num2
print('Sum is:', sum)
print('Product is:', product)
print('Difference is:', difference)
print('Quotient is:', quotient)
print('-----------------------------------')
print('Handling Division and Float Precision')
numerator = 10.0
denominator = 3.0
result = numerator / denominator
print('Result of division:', result)
print('Result rounded to 2 decimal places:', round(result, 2))
print('-----------------------------------')
print('printf Style Formatting')
language = 'Python'
version = 3.10
print(f'I am learning {language} version {version}.')

print('-----------------------------------')
print('Python program that asks the user for the radius of a circle and calculates the area using the formula: Area = π * radius^2.')
import math
radius = 4
area = math.pi * radius ** 2
print('The area of the circle with radius', radius, 'is:', area)



