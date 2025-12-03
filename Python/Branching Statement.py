# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))

# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")

# ######################################

# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are a minor.")
# elif 18 <= age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# ######################################

# Nested if-else example

num = 10

if num > 10:
    print("Number is greater than 10")
    if num > 20:
        print("Number is also greater than 20")
    else:
        print("Number is not greater than 20")
elif num == 10:
    print("Number is equal to 10")
elif num == 20:
    print("Number is equal to 20")
else:
    print("Number is below than 10")
