# function

def wishes(name):
    print(f"Hello {name}, Good Morning!")

wishes("John")

def greetings():
    print("Good Moring Everyone!")

greetings()

def wishes_with_Return(name):
    print(f"Hello {name}, Good Afternoon!")

wishes_with_Return("Shaaan")

def greetings_in_Detail(name,age,clg,rollNo):
    print(f"Hello {name}, You are {age} years old. You are from {clg} and your roll no is {rollNo}")

greetings_in_Detail("Mirzan",20,"VIT",18)

print("##########################################################")
# return functions

def addition(a,b):
    return a + b

result = addition(5, 10)
print("Addition Result:", result)


def subtraction(a,b):
    return a - b

result2 = subtraction(15, 5)
print("Subtraction Result:", result2)

def multiplication(a,b):
    return a * b

result3 = multiplication(4, 6)
print("Multiplication Result:", result3)

def division(a,b):
    return a / b

result4 = division(20, 4)
print("Division Result:", result4)

print("##########################################################")

a=10
print(a)
a=20
print(a)


def greet(name="Guest"):
    print(f"Hello, {name}! students of SSITS")

greet("Alice")  # uses the provided name "Alice"
greet() # uses the default value "Guest"

# Args and Kwargs arguments

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5))