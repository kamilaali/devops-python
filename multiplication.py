from unicodedata import digit


a=123
# find the multiplication of digits of the number a
# when we find the remainder with 10 it will give us the last digit of the number
# when we divide the number by 10 it will remove last digit
last_digit =a%10 #3

a=a//10


middle_digit =a%10
a=a//10
frist_digit  =a%10
multiplication=last_digit*middle_digit*frist_digit
print("muliplication of number a ", (multiplication ))