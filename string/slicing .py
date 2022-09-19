from shutil import which


print("inter atring whichlength is oddand longer than 4 letters")
text=input()
midlle_index=len(text)//2
print()


#    0123456789
s = "Techtorial"

print(s[4:7])

print(s[4]+s[7])

# Ask user the enter a string which length is odd and longer than 3
# and print the middle three letters from the string

# "Chicago"  -> ica
# "seven"    -> eve


print("Enter a string which length is odd and longer than 3 letters")
text = input()
# First I have to find middle index
middle_index = len(text) // 2     # int(len(text)/2)

print(text[middle_index-1:middle_index+2])


Yusuf CT
  7:47 PM
# Ask user the enter a string which length is even and longer than 4
# and print the middle 4 letters from the string

# techtorial ->  htor
# keyboard   ->  yboa

print("user the enter a string which length is even and longer than 4")
text1 = input()

middle_index = int(len(text1) / 2)
print(text1[middle_index-2:middle_index+2])







