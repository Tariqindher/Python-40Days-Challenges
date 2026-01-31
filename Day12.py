
#List: A mutable (changeable), ordered collection that can store duplicate items.
#Tuple: An immutable(Not changeable), ordered collection that can store duplicate items.
#Set: A mutable, unordered collection of unique items.
#Dict: A mutable, ordered (≥3.7) collection of key-value pairs with unique keys.


numbers=[11,33,22,44,77,88]
#print the list
print(numbers)
#print the element at index 3
print(numbers[3])
#print the last element of the list
print(numbers[-1])
#print the first 3 elements of the list
print(numbers[:3])
#print the element after 2 index 
print(numbers[2:])
#print after 2 each element
print(numbers[::2])

#sort the list
numbers.sort()
print(numbers)

#Reverse the list
numbers.reverse()
print(numbers)

#length of list
print(len(numbers))


#Add new element at the end of the list

numbers.append(99)

#Remeove element from the list use Remove
numbers.remove(44)

#insert an element at specfic position 
numbers.insert(2,65)
print(numbers)

#Remove all elements from the list use clear methods
numbers.clear()
print(numbers)

# New list
fruits= ["apple", "banana","carrot", "Orange"]

#Find banana from the list
if "banana" in fruits:
        print("Items Found in the list")
else :
        print("Items Not found in the List")

#create a list of squares of numbers from 1 to 5 
# Use list

squares=[x**2 for x in range(1,6)]
print(squares)


#Nested List print the sublist
nestedList=[[1,2],[4,5],[6,7]]

for sublist in nestedList:
        print(sublist)
        
        



