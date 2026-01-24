#For loop

for i in range(1,10):
            print(i, end=' ')

print()
text="Tariq"

for  ch in text:
       print(ch,end =" ")

print()
#Print even number
for i in range(2, 22,2):
      print(i , end=" ")
print()

fruits=["apple", "Banana", "Cherry"]
print(fruits)

for i in fruits:
      print(i , end=" ")

number=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in number:
      sum=sum+i
print("The Sum: ", sum)

#Nested Loop
for i in range(1,10):
     for j in range(1,10):
           print(f'{i}*{j} = {i*j}')
     print()

#Skip 3 
for i in number:
        if i==3:
             continue
        print(i , end=" ")

#Looping with enumerate
colors = ["black", "green", "white", "Red"]
print()
for index, color in enumerate (colors):
                print(f' {index} : {color}')

#Loop Over Multiple Lists
names = ['Alice', 'Bob', 'Charlie'] 
scores = [85, 90, 95] 
for name, score in zip(names, scores): 
print(f'{name}: {score}')

numbers = [1, 2, 3, 4, 5] 
for num in numbers: 
if num == 10: 
print('Found 10') 
break 
else: 
print('10 not found') 

squares = [x ** 2 for x in range(1, 6)] 
print(squares) 
 








             