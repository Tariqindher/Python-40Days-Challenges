#Functions and List
def greet():
     print("Hello Tariq")

greet()

def add(a,b):
     return a+b

print(f'The sum is: {add(4,5)}')


#Function with defualt arfuments

def greet(name, greeting='Assalam O Alaikum'):
     print(f'My name is :{name}, {greeting}')

greet('Tariq')
greet("Tariq",'Hi')

#Sum All

def sum_all(*numbers):
     return sum(numbers)

print(sum_all(2,3,4,5))


def find_max(a, b, c): 
  return max(a, b, c) 
print(find_max(10, 15, 5))

def factorial(n): 
   if n == 0: 
    return 1 
   else: 
    return n * factorial(n - 1) 
   
print(factorial(5))

     
     
     