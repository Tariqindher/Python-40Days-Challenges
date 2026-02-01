#Tuple: An immutable(Not changeable), ordered collection that can store duplicate items.
#Dict: A mutable, ordered (≥3.7) collection of key-value pairs with unique keys.
my_tuple = (1, 'apple', 3.5)
print(my_tuple)
#Access element using index
print(my_tuple[0])

#Unpack tuple into Seprate Variables

my_tuple =('Apple','Banana', 'Carrot')
print(my_tuple)
fruit1, fruit2, fruit3 = my_tuple

print(fruit1,fruit2,fruit3)

#Modify an element it will error bcz it is immutable
#my_tuple[0]='A'
print(my_tuple)


#Function 

def calculate(numbers):
     total = sum(numbers)
     avg = total/len(numbers)
     return total, avg


result  = calculate((1,2,3,4,5,6))
print(f'Sum and Average :{result} ')



#Dictionary
person = { 'name' :'Tariq', 'age':22, 'city' : 'sukkur'}
print(person['name'])


#Add email
person['email']= 'indhertariq83@gmail.com'
print(person)
#Remove the city
del person['city']

#Print key and value using loop

for key, value in person.items():
     print(f'{key} : {value}')

#A dictionary with multiple values for each key 

person = {'name':['Tariq','Gul'], 'city':['PanoAKil','Sukkur']}
print(person)

#Merge two dictionaries

dict1={'name':'Tariq', 'Age':22}
dict2={'City':'Sukkur', 'email':'indhertariq83@gmail.com'}

dict1.update(dict2)
print(dict1)
#Dictionary in function
def describe_person(person): 
     for key, value in person.items(): 
      print(f'{key}: {value}') 

person = {'name': 'Alice', 'age': 30, 'city': 'New York'} 
describe_person(person)

#Nested Dictionary

people = { 
'Alice': {'age': 30, 'city': 'New York'}, 
'Bob': {'age': 25, 'city': 'Chicago'} 
} 
print(people)



 


