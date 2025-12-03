# List
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))

print(fruits[0])  # Accessing first element
print(fruits[1])  # Accessing second element
print(fruits[-1]) # Accessing last element

fruits.append("orange")  # Adding an element
fruits.insert(4, "pineapple")  # Inserting at specific position
fruits.remove("banana")  # Removing an element
fruits.pop()  # Removing last element
print(fruits)

name = ["Alice", "Bob", "Charlie"]

name.append("David")
name.remove("Bob")
name.insert(1, "Eve")
name.pop()

print(name[0])
print(name[-1])
print(name)

# tuple
numbers = (1, 2, 4, 4, 5)
print(type(numbers))                 
print(numbers)
print(numbers.count(4)) # how 4 are there shows in this case 2 
print(numbers.index(5)) # shows index of 5 which is 4
print(len(numbers))# shows length of tuple which is 5
print(max(numbers)) # shows maximum number which is 5
print(min(numbers)) # shows minimum number which is 1

# set
s = {1, 2, 3, 4, 4, 5}
print(type(s))
print(s)  # Duplicates will be removed
s.add(6)  # Adding an element
s.remove(3)  # Removing an element
s.update([7, 8, 9])  # Adding multiple elements
s.pop()  # Removing an arbitrary element (any value can be removed)
print("Added and Removed after value:\n", s)

s2 = {4, 5, 6, 7, 8}
print(s2)
s2.add(1)
s2.remove(7)
s2.pop()
s2.update([10, 11])
print("Added and Removed after value:\n", s2)

# dictionary

dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}

print(type(dict1))
print(dict1)
print(dict1["name"])  # Accessing value by key
print(dict1.get("age"))  # Accessing value by key using get()
print(dict1.keys())  # Getting all keys
print(dict1.values())  # Getting all values

dict1.update({"State": "NY"})  # Adding a new key-value pair
print(dict1)

del dict1["city"]  # Removing a key-value 
print(dict1)

dict2 = {
    "name": "Bob",
    "age": 30,
    "city": "San Francisco",
}
print(type(dict2))
print(dict2)

print(dict2["name"])
print(dict2.get("age"))
print(dict2.keys())
print(dict2.values())

dict2.update({"State": "CA"})
print(dict2)

del dict2["city"]
print(dict2)

# Slice

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

slice1 = my_list[0:6]

print("Original List:", my_list)
print("Sliced List (0 to 5):", slice1)

slice2 = my_list[0:10:2] # index 4 to index 9 with skipping 1 element picking the next
print("Sliced List (4 to 9 with step 2):", slice2)

slice3 = my_list[:5]  # From start to index 4
print("Sliced List (start to 4):", slice3)

slice4 = my_list[:-1]
print("Sliced List removed last element",slice4)

slice5 = my_list[0:-1:3]
print("Sliced List (0 to -1 with step 3):", slice5) # skipping 2 elements and picking the 3rd one

