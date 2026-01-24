#Combining Control Flow and Loops

for i in range(1, 11): 
  if i % 2 == 0: 
       print(i)

for i in range(1, 31): 
         if i % 3 == 0 and i % 5 == 0: 
               print('FizzBuzz') 
         elif i % 3 == 0: 
               print('Fizz') 
         elif i % 5 == 0: 
               print('Buzz') 
         else: 
               print(i)

for i in range(1, 6): 
      for j in range(1, 6): 
          if j == 3: 
             break 
          print(i, j) 
          if i == 4: 
             break