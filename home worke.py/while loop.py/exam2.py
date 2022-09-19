# from re import S


# print("enter the frist number")
# S=input()
# print("enter the scocond number")
# s2=input()
# if s# Ask user to enter an integer number and
#  print out all the divisors of given integer number
# 6 -> divisors of six 1,2,3,6
# 10 -> 1,2,5,10
# 14 -> 1,2,7,14
# 11 -> 1, 11

# Possible dividers of given number.
# starts from 1 -> ends at the given number itself

print("Enter a number")
num = int(input())

possible_divisor = 1
s = ""
while possible_divisor <= num:
    #Since we have the possible divisor, but we are not sure 
    # If we can divide the number or not. 
    #How can I understand if possible_divisor is an actual divisor of the number?
    #if number % possible divisor is 0 it means possible_divisor
    #  is an actual divisor of the number
    if num % possible_divisor==0:
        s+=str(possible_divisor)+", "
    possible_divisor+=1
# Remove suffix only removes if the string is ending with given charachters.
print(s.removesuffix(", "),"are the divisors of the number")
#I want to print all divisors in one line like following example
#"1,2,3,6 are the divisors of the number"

1 reply
2 days agoView thread


Yusuf CT
  1:06 PM

# Ask user to enter an integer number 
# and print multiplication table for given number

# 3 * 1 = 3 
# 3 * 2 = 6  
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# .....
# .....
# 3 * 10 = 30

print("enter a number")
num = int(input())

#  to use the loop i need to find the range
# On which number multiplication table starts - 1
# On which multiplication table ends - 10

table_num = 1
while table_num<11:
    print(f"{num} * {table_num} = {num*table_num}")
    table_num +=1
    
New


Yusuf CT
  6:07 PM

# Ask user to enter their age
# print out your age is {age}
# till their age gets to 60
print("Enter your current age")
age = int(input())

# Their age should be smaller equal to 60

while age <=60:
    print(f"Your age is {age}")
    age+=1


Yusuf CT
  6:29 PM


# Ask user to enter two numbers, first is greater than the second one. 
# Find out sum of all the numbers between given two numbers not inclusive. 3
# first number is 7
# second number is 3
#  4 5 6  -> 15 
# first number is 9
# second number is 6
# 6    7 8     9  -> 15
# first num 11
# second num is 7
# 7    8 9 10     11 -> 27 
print("Enter a number")
num1 = int(input())
print("Enter a number smaller than first one")
num2 = int(input())

#Before we get to the sum let's print all the numbers between given two number
copyOfnum2 = num2
num2 = num2 +  1
sum = 0
while num2 < num1:
  #  print("In the loop",num2)
  sum += num2
  num2 = num2 +1
print(f"Sum of the numbers between {num1} and {copyOfnum2} is {sum}")  











q '"




