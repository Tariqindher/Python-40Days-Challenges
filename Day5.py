#Write a Python program that generates a random number between 1 and 100 and asks the 
#user to guess the number. 

import random 
number = random.randint(1, 100) 
print("I have selected a number between 1 and 100. Can you guess it?") 
while True: 
          guess = int(input("Enter your guess: ")) 
          if guess < number:           
                    print("Too low! Try again.") 
          elif guess > number: 
                    print("Too high! Try again.") 
          else: 
                    print(f"Congratulations! You guessed the number: {number}.") 
                    break 
