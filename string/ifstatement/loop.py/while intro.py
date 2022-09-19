num =1
while num<=10:
   print(num)
   num=num+1
   



num2 =2
while num2 <=10:
   print(num2)
   num2=num2+2
#    print even number that are smaller equal to 10
#this time variable num is going to start from 1
num=1 
while num <=10:
    if num%2==0:
        print(num )
        num+=1

        
# In the factory we need to create a program that can 
# find if we can do the shipment and if we can do the shipment
# it will tell use how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages. 

# count of small package = 4 -> 4 kilogram
# count of big package = 1 -> 5 kilogram 
# goal is to ship 9 kilogram 
# i can ship and i need to use 4 small package

# 5 small package-> i need to use 3 smal package
# 4 big package  -> how many big package i need to use -> 2
# I need to ship 13 kilogram 
# i can ship and i need to use 3 small package

# 3 small package-> i need to use 4 small package to complete but since i don't 
# have 4 small package i cannot ship
# 3 big package -> i can use max 2 big package
# i need ship 14 kilogram
# I cannot ship

print("Enter the kilogram we need to ship")
goal_ship = int(input()) # 12

print("Enter amount of small packages you have")
count_of_small = int(input())

print("Enter amount of big packages you have")
count_of_big = int(input())

# I have to start from big packages to reach goal kilogram
# How can I find how many big package i need to reach to goal?

needed_big_packages = goal_ship // 5


# If I don't have enough big packages can I do the shipment-No

# 9 small package
# 1 big package 
# I need to ship 14 kilogram
if needed_big_packages<=count_of_big:
    #How many small package i need
    needed_small_packages = goal_ship%5
    if needed_small_packages <= count_of_small:
        print(f"I can do the shipment and i need {needed_small_packages} amount of small package")
    else:
        print("I cannot do the shipment")
else:
    # How many kilogram can I reach with the big boxes i have  and then the rest of the amount i will 
    # try to complete with using small packages
    kilogram_i_have = count_of_big * 5;
    left_goal = goal_ship - kilogram_i_have
    # Left goal divided by 1 will give amount of small package i need 
    if left_goal<=count_of_small:
        print(f"I can do the shipment and I need {left_goal} amount of small boxes")
    else:
        print("i cannot do the shipment.")


Yusuf CT
  11:54 AM

# Print numbers from 1 to 10 inclusive
num =1
while num<=10:
    print(num)
    # I have to update the value of variable num in the loop so 
    # condition will become false eventually. 
    num = num + 1
print(f"Value of the variable num is {num}") # 11
# Print even numbers that are smaller equal to 10
num = 2
while num <= 10:
    print(num)
    num = num + 2
print(f"Value of the variable num is {num}") # 12


# Print even numbers that are smaller equal to 10
# This time variable num is going to start from 1
num = 1
while num <= 10:
    if num%2==0:   # This line is in the while loop
        print(num) # This line is in the while as well as in the if statement   
    num +=1        # This line is in the while loop

#Line below is there for to understand what value the variable num will take 
# after the loop above.
print(num) # 11

# From 1 to 20 inclusive, print every odd number in following format
# "This is an odd number {Value of number}"
# print every even number 
#"This is an even number {Value of number}"

num = 1
while num <=20:
    #In the while loop I have to decide num is currently even or odd
    if num % 2==1:                               #This line is in only while loop
        print(f"This is an odd number {num}")    #This line is in while loop also in if
    else:                                        #This line is in only while loop
        print(f"This is an even number {num}")   #This line is in while loop also in if
    #I have to update the value of the number
    num +=1                                      #This line is in only while loop 

#Example of an infinite loop.
# num =0
# while num < 1:
#     print("in the while loop")                     #This line is in the while
# print("Outside the while after the infinite loop")  #This line is outside the while
New


Yusuf CT
  12:17 PM

# Ask user to give you a string
# From that string print index numbers of all the e's
#  
print("Enter a text")
str = input()

# We can access string elements using their indexes.
index = 0

# Index number is always smaller than length of the string.
#"Example"
# 0123456  Index numbers
#   7  Length of the string
length_of_str = len(str)

while index < length_of_str:
    # I want to acces the element with index number str[index]
    if str[index] == "e":
        print(f"Index number of e is {index}")
    index+=1









q '"











    

