from operator import length_hint


print("enter any string have spaces")
str=input()
str=str.replace(" ","")
print(str.replace(" ",""))
length=len(str)
if length%2==0:
    print(False)
else:
    print(True)