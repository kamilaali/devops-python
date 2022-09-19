num=[1,2,3,1,2,3,4,2,2,2]
new_num=num.copy()
for  number in new_num:
    if number==2:
        num.remove(2)
print(num)
