import random
#Week 02 Control Flow and Looping 
# While Loop
counter=0
while counter < 5:
          print(counter, end=' ')
          counter=counter+1
print()
#Break in Loop
num=10
while num>0:
          if num<5:
            break
          print(num, end=' ')
          num=num-1
print('\nEnd the Loop')


#Continue , Skip the Print 5

num=10
while num>0:
           if num==5:
               num=num-1
               continue
           print(num, end=' ')
           num=num-1

print()
#Print Simple Multiplication Table (1 to 5) Nested Loop

i=1
while i<=5:
          j=1
          while j<=5:
                 print(i*j, end='\t')
                 j+=1
          print()
          i=i+1

print()

counter=0
while True:
          print(f'counter: {counter} ')
          counter=counter+1
          if counter>5:
             break
print()

correct_answer=7
guess=-1
while guess!=correct_answer:
          guess = int(input('Guess the Number (1-10): '))
print('You guessed correctly!')


#Else Block with While loop
counter=0
while counter < 5:
          print(f'counter :{counter} ')
          counter=counter+1
else: 
      print(' Loop Finished SuccessFully! ')
print()

#Create a number-guessing game where the user has
#a limited number of attempts to guess a random number.

target = random.randint(1, 10)
attempts = 3
while attempts >=1:
              guess= int(input('Guess the number (1-10)'))
              if guess == target:
                  print('Correctly,  You won.')
                  break
              else:
                      print(f'Wrong! You have {attempts-1 } attempts left')
                      attempts=attempts-1
else :
        print(f'Sorry, the Number was target :{target}')




          


                    