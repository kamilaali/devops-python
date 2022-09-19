# Write a program that will accept 5 digit number and
# will print reversed number at the end.
# Example-1:
# 53876
# The output is 67835
# Example-2:
# 97352
# The output is 25379
a=53876
digit_number_5= a%10
print(digit_number_5)
a=a//10
digit_number_4=a%10
print(digit_number_4)
a=a//10
digit_number_3=a%10
a=a//10
digit_number_2=a%10
a=a//10
digit_number_1=a%10
print(digit_number_5,digit_number_4,digit_number_3,digit_number_2,digit_number_1)