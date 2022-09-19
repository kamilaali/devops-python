# Ask user to enter a string
# if the given string contains any duplicated letter
# print string has duplicated letter 
# otherwise print string consists of unique letters. 

print("Enter a string")
str = input()

# we should check for each letter, if there is duplication
is_unique = True
index =0
while index<len(str):
    if str.count(str[index])>1:
        # it means there is duplicated letter
        is_unique = False
        break
    index+=1

if is_unique==True:
    
    print("String consists of unique letters")
else:
    print("String has duplicated letters")    
white_check_mark
eyes
raised_hands
React
Reply









# ask usser duplicate# ask user a given string duplicate each letter in the given string
# input abc 
# output aabbcc
# input def
# output ddeeff

print("Enter a string")
str = input()

duplicated =""

for l in str:
    duplicated=duplicated+l
    print("THis print shows evolution of the duplicated",duplicated)
    duplicated=duplicated+l
    print("THis print shows evolution of the duplicated",duplicated)
print(duplicated)









