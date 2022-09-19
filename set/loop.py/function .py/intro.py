# When we want to reuse the piece of code or algorithm, 
# we create functions and reuse them . 

# syntax of creating a function is -> def method_name. 

def print_name():
    print("Techtorial.")

# Methods only work when they get called. 
print_name()

# Let's create a method for greeting. 
# It will take user's name as argument and will print,
#Hello User'sName
def print_greeting(name):
    print(f"Hello {name}")

print("Enter your name ")
user_name = input()
print_greeting(user_name)



# Let's create a method for greeting. 
# It will take user's name as argument and will print,
#Hello User'sName
def get_greeting(name):
    return f"Hello {name}"
# Methods includes what is indented but it is recommended to leave 
# 2 lines of space after the last line of method. 
print(type(get_greeting("John")))
greeting1 = get_greeting("John")
print("TYpe of greeting is",type(greeting1))
print(greeting1)

print(get_greeting("Yusuf"))
print(get_greeting("Sofi"))
print(get_greeting("Stevie"))



# Create a method to find sum of given two integers. 
# Given means the method will take it as parameter. 
# Add an if statement in this method so it will print error occured 
# if type of num1 or type of num2 is not float or integer. 
def sum(num1,num2):
    addition = num1 + num2
    s     = str(type(addition))
    if "int" in s or "float" in s:
        return addition
    else:
        return "An error occured."

    # if type(num1 + num2)
    # return 
# Methods will always stop when the code reaches the return statement. 

print(sum("A","B"))
print(sum(1,3))