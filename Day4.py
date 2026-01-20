num = 10
if num>0:
        print("Positive Number")

if num%2==0:
         print("Even")
else:
        print("Odd Number")

print('-----------------------------------')
if num>0:
        print("Positive Number")
elif num<0:
        print("Negative Number")
else:
        print("Zero")

print('-----------------------------------')
#Write a Python program to check eligibility for a discount based on age and membership status.

age =18
memebership_status = True

if age >=18:
        if(memebership_status):
                print("You are eligible for 20% discount.")
        else:
                print("You are  eligible for 10% a discount.")
else:
        if(memebership_status):
                    print("You are eligible for 15% discount.")
        else:
                print("You are elifible for 5% discount.")
print('-----------------------------------')
#Using Loops
i=1

while i<=10:
        print(i)
        i+=1
print('-----------------------------------')
for i in range(1,11):
                    print(i)
print('-----------------------------------')

#Use Break and Continue Statements
# while True:
#         num=int(input("Enter a number (0 to stop): "))
#         if num==0:
#                     break
#         print(f'You entered: {num}')

for i in range(1,11):
        if i%2==0:
                    continue
        print(i)
print('-----------------------------------')

#Using else with loop
for i in range(1,11):
        if i%5==0:
             print(f'{i} is divisible by 5')
             break
else:
        print ("No Number divisible by 5 found")

#Check Number is Prime or Not

num =7

if num>1:
        for i in range (2, num):
                if num%i ==0:
                    print(f'{num} is Not Prime Number')
                    break
        else:
             print(f'{num} is Prime Number')
else :
        print(f'{num} is Not Prime Num')

#Write a Python program that calculates the sum of numbers from 1 to 100 using a loop.
sum = 0
for i in range(1,101):
        sum=sum + i
print(sum)

#Write a Python program that calculates the factorial of a number using a loop. 
n=4
factorial = 1
for i in range(1,n+1):
        factorial=factorial*i
print(factorial)



#Write a Python program that asks the user for a string and prints the string in reverse.
word='Tariq'
rev =''
for char in word:
        rev = char + rev 
print("Reverse String ",rev)

#Write a Python program that checks if a given string is a palindrome.
original='madam'
rev=''
for ch in original:
        rev = ch + rev

if(original==rev):
        print(f'Word: {original} is palindrome')
else : 
        print(f'Word: {original} is not palindrome')

#Write a Python program that prints the numbers from 1 to 50. For multiples of 3, print 'Fizz', for multiples of 5, print 'Buzz', and for multiples of both, print 'FizzBuzz'.

for i in range(1,51):
        if(i%3 == 0 and i%5 == 0):
                print("FizzBuzz")
        elif(i%3==0):
                print("Fizz")
        elif(i%5== 0):
                print("Buzz")



#Write a Python program that prints the multiplication table for numbers 1 through 10.

for i in range(1,11):
        print(f'2 * {i} = {2*i}')


#Write a Python program that calculates the sum of all even numbers from 1 to 100. 
sum=0

for i in range(1,101):
        if (i%2==0):
                sum=sum+i
print(f'The sum of all even numbers from (1 to 100):  {sum}')

#Write a Python program that takes three numbers from the user and prints the largest one. Teach about max() function. 
n1=47
n2=98
n3=9
print("The Largest No:",max(n1,n2,n3))

#Write a Python program that counts the number of vowels in a given string. 
word="abcdefghijklmnopqrstuvwxyzAEIOU"
vowel='aeiouAEIOU'
count=0
for ch in word:
        if ch in vowel:
                count=count+1

print(count)










